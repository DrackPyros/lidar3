import time
import math
import datetime
import PyLidar3
import matplotlib
import ctypes as c
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import multiprocessing as mp
from matplotlib.animation import FuncAnimation
matplotlib.use("TkAgg")

def plot_stream(interval):
    fig = plt.figure(figsize=(6, 6))
    ax = plt.subplot(111)
    _ = FuncAnimation(fig, draw_scan, interval=interval, fargs=[ax])
    plt.show()

def draw_scan(_, ax):
    cs = np.frombuffer(mp_arr.get_obj()).reshape((360, 2))
    ax.clear()
    ax.scatter(cs[:, 0], cs[:, 1], c='b', s=5)
    ax.scatter(0, 0, c='r', s=5)
    ax.set_ylim(-6000, 6000)
    ax.set_xlim(-6000, 6000)

def adjust_frequency(hertz=10):
    curr_f = Obj.GetCurrentFrequency()
    while curr_f != hertz:
        if curr_f <= hertz - 1:
            Obj.IncreaseCurrentFrequency(frequencyStep=PyLidar3.FrequencyStep.oneHertz)
        elif curr_f >= hertz + 1:
            Obj.DecreaseCurrentFrequency(frequencyStep=PyLidar3.FrequencyStep.oneHertz)
        elif hertz - 1 < curr_f < hertz:
            Obj.IncreaseCurrentFrequency(frequencyStep=PyLidar3.FrequencyStep.oneTenthHertz)
        elif hertz < curr_f < hertz + 1:
            Obj.DecreaseCurrentFrequency(frequencyStep=PyLidar3.FrequencyStep.oneTenthHertz)
        curr_f = Obj.GetCurrentFrequency()
        print(f'Adjusting frequency to {curr_f}Hz')

def adjust_ranging_frequency(khertz=9):
    curr_f = Obj.GetCurrentRangingFrequency()
    while curr_f != khertz:
        Obj.SwitchRangingFrequency()
        curr_f = Obj.GetCurrentRangingFrequency()
        print(f'Adjusting ranging frequency to {curr_f}Hz')
    
if __name__ == '__main__':    
    show_plot = True
    plot_redraw_interval = 500
    port = '/dev/ttyUSB0'
    Obj = PyLidar3.YdLidarG4(port, chunk_size=6000)
    mp_arr = mp.Array(c.c_double, 360 * 2)
    coords = np.frombuffer(mp_arr.get_obj()).reshape((360, 2))

    if Obj.Connect():
        print(Obj.GetDeviceInfo())
        adjust_frequency(hertz=7)
        print(f'Device current frequency is {Obj.GetCurrentFrequency()}Hz')
        adjust_ranging_frequency(khertz=9)
        print(f'Device current ranging frequency is {Obj.GetCurrentRangingFrequency()}kHz')        
        
        if show_plot:
            plot_process = mp.Process(target=plot_stream, args=(plot_redraw_interval, ))
            plot_process.start()

        gen = Obj.StartScanning()
        df = pd.DataFrame()
        current_hour = datetime.datetime.now().hour
        old_ts = time.time_ns()
        while True:
            scan_data = next(gen)
            row = {}
            for angle in range(360):
                row[f'{angle:03d}'] = scan_data[angle]
                if show_plot:
                    if scan_data[angle] > 100:
                        coords[angle, 0] = - scan_data[angle] * math.cos(math.radians(angle))
                        coords[angle, 1] = scan_data[angle] * math.sin(math.radians(angle))
                    else:
                        coords[angle, :] = 0
            ts = time.time_ns()
            row['timestamp'] = ts
            # print(f'{1e9/(ts - old_ts):.2f}')
            old_ts = ts
            df = df.append(row, ignore_index=True)
            if datetime.datetime.now().hour != current_hour:
                filename = f'{time.strftime("%Y_%m_%d_%H_%M_%S")}_g4.csv'
                df.to_csv(filename, index=False)
                df = pd.DataFrame()
                current_hour = datetime.datetime.now().hour