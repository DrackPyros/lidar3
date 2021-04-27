import pandas as pd
import PyLidar3
import time
import matplotlib.pyplot as plt
import matplotlib
import math
from datetime import datetime


port = "/dev/ttyUSB0"
Obj = PyLidar3.YdLidarX4(port, chunk_size=5000)  #PyLidar3.your_version_of_lidar(port,chunk_size)

interval = 0.5 # saving interval in hours

t_alive = 1 # tiempo funcionando horas

df = pd.DataFrame(dtype=int)

if(Obj.Connect()):
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    t = time.time() # start time 
    t_save = time.time() # tiempo guardar

    now = datetime.now()
    h_inicio = now.strftime("%d\\%m\\%Y %H:%M:%S")

    while (time.time() - t) < t_alive*3600: #scan for 10 mins
        data = next(gen)
        mydata = {}
        for angle in range(360):
            mydata[f'{angle:03d}'] = int(data[angle])
        mydata['timestamp'] = int(time.time() * 1e3)
        df = df.append(mydata, ignore_index=True)

        if (time.time() - t_save) >= interval*3600: #save 1 mins
            now = datetime.now()
            h_fin = now.strftime("%H:%M:%S")
            archivo = "files/"+h_inicio + ' - ' + h_fin+'.csv'
            # print(archivo)
            df.to_csv(archivo, index=False, mode="a")
            df = pd.DataFrame(dtype=int)
            t_save = time.time()

    Obj.StopScanning()
    Obj.Disconnect()

else:
    print("Error connecting to device")


