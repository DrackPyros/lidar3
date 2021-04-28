# import numpy as np
# a = np.arange(15).reshape(3, 5)

# print(a)

# # array([[ 0,  1,  2,  3,  4],
# #        [ 5,  6,  7,  8,  9],
# #        [10, 11, 12, 13, 14]])

# print(a.shape) # (3, 5)

# print("Dimensiones: "+a.ndim) # 2

# # print(a.dtype.name) # 'int64'

# # print(a.itemsize) # 8

# # print(a.size) # 15

# # print(type(a)) # <class 'numpy.ndarray'>

# # ---------------------------------------

# # b = np.array([6, 7, 8])

# # print(type(b)) # <class 'numpy.ndarray'>
# -----------------------------------------------------------
# import time
# from datetime import date

# print (str(time.asctime()))
# from datetime import datetime

# now = datetime.now()
 
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print(dt_string)	

# current_time = now.strftime("%H:%M:%S")
# archivo = dt_string + ' - ' + current_time
# print(archivo)
# print(type(archivo))

# print(now())

#-----------------------------------------------------------------
import numpy as np
import pandas as pd
import os
import math

filename = os.path.join("..", "files", "26_04_2021_13:09:15_13:09:51.csv")
data = pd.read_csv(filename)


# x = [20000, 20000, data.shape[0]]

matriz = np.zeros(shape=[2000, 2000, data.shape[0]], dtype=float, order='C')
for index, row in data.iterrows():
    for angle, value in enumerate(row[:-1]):
        x = int(value * math.cos(math.radians(angle))//10)+1000
        y = int(value * math.sin(math.radians(angle))//10)+1000
        # print(x, y)
        matriz[y, x, index] = 1
    exit()
# print(matriz)

