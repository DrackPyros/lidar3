import pandas as pd
import PyLidar3
import time
import matplotlib.pyplot as plt
import matplotlib
import math
from datetime import datetime


port = "/dev/ttyUSB0"
Obj = PyLidar3.YdLidarX4(port, chunk_size=5000)  #PyLidar3.your_version_of_lidar(port,chunk_size)

t_save = 0.5 # Saving interval in hours

t_alive = 1 # Running time in hours

df = pd.DataFrame(dtype=int)

if(Obj.Connect()):
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    t = time.time() # Time check 
    s = time.time() # Saving check

    now = datetime.now()
    t_start = now.strftime("%Y_%m_%d_%H:%M:%S")

    while (time.time() - t) < t_alive*3600:
        data = next(gen)
        mydata = {}
        for angle in range(360):
            mydata[f'{angle:03d}'] = int(data[angle])
        mydata['timestamp'] = int(time.time() * 1e3)
        df = df.append(mydata, ignore_index=True)

        if (time.time() - s) >= t_save*3600:
            now = datetime.now()
            t_end = now.strftime("%H:%M:%S")
            name = "files/"+t_start + '-' + t_end+'.csv' # File path & name
            df.to_csv(name, index=False, mode="a")
            df = pd.DataFrame(dtype=int)
            s = time.time()

    Obj.StopScanning()
    Obj.Disconnect()

else:
    print("Error connecting to device")


