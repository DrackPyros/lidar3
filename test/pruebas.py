import threading
import PyLidar3
import matplotlib.pyplot as plt
import math    
import time
import csv
import pandas as pd

# import numpy as np

def dibujar():
    global is_plot
    while is_plot:
        plt.figure(1)
        plt.cla()
        plt.ylim(-9000,9000)
        plt.xlim(-9000,9000)
        # plt.scatter(x,y,c='r',s=8)
        plt.pause(0.001)
    plt.close("all")

def escribir1(): # Escribir resultado de prueba en un txt
    with open('a.txt', 'w') as file:
        file.write("Eje X: ")
        file.write(str(x))

def escribir2():
    salir = False
    while salir == False:
        try:
            with myFile:
                df = pd.DataFrame(x, columns=[tiempo]) # Cada columna tiene de primera celda el timestamp
                df.to_csv(n_archivo, index=False) 
            salir = True
        except IOError:
            open(n_archivo, 'x')

def escribir():
    salir = False
    while salir == False:
        try:
            with open('data.csv', 'w'):
                # string = separator.join(x)

                spamwriter = csv.writer(n_archivo, delimiter=',')
                # for row in spamwriter:
                spamwriter.writerow(', '.join(x))
            salir = True
        except IOError:
            open(n_archivo, 'x')

    

n_archivo = 'data.csv'
myFile = open(n_archivo, 'w')
is_plot = True
x = []
n_vueltas = 0

port = "/dev/ttyUSB0"
Obj = PyLidar3.YdLidarX4(port, chunk_size=5000)  #PyLidar3.your_version_of_lidar(port,chunk_size)

for _ in range(360):
    x.append(0)

# threading.Thread(target=draw).start()

if(Obj.Connect()):
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    t = time.time() # start time 
    while (time.time() - t) < 2: #scan for 2 seconds
        data = next(gen)

        n_vueltas += 1

        for angle in range(360):
            x[angle] = data[angle]
        tiempo = time.time_ns()
        escribir()

    is_plot = False
    Obj.StopScanning()
    Obj.Disconnect()

    print(n_vueltas) # Tiene que coincidir con el numero de columnas

else:
    print("Error connecting to device")
