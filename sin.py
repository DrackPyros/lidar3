# import numpy as np
import time
# from datetime import date
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


# print (str(time.asctime()))
from datetime import datetime

now = datetime.now()
 
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print(dt_string)	

current_time = now.strftime("%H:%M:%S")
archivo = dt_string + ' - ' + current_time
print(archivo)
print(type(archivo))

# print(now())