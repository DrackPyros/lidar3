import PyLidar3
import matplotlib.pyplot as plt
import matplotlib
import math
import _thread

matplotlib.use("TkAgg")

def plotting_thread(fig, axe, gen):
    while True:
        x = [0 for _ in range(360)]
        y = [0 for _ in range(360)]

        data = next(gen)
        for angle in range(360):
            if data[angle] > 100:
                x[angle] = - data[angle] * math.cos(math.radians(angle))
                y[angle] = data[angle] * math.sin(math.radians(angle))
        axe.clear()
        axe.scatter(x, y, c='b', s=5)
        axe.scatter(0, 0, c='r', s=5)
        axe.set_ylim(-6000, 6000)
        axe.set_xlim(-6000, 6000)
        fig.canvas.draw_idle()

port = '/dev/ttyUSB0'
Obj = PyLidar3.YdLidarX4(port, chunk_size=5000)
if Obj.Connect():
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()

    fig = plt.figure(1)
    axe = fig.add_subplot(111)
    plt.cla()
    _thread.start_new_thread(plotting_thread, (fig, axe, gen))
    plt.show()
else:
    print("Error connecting to device")
