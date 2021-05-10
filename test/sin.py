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
# -----------------------------------------------------------

import numpy as np
import pandas as pd
import os
import math
import matplotlib.pyplot as plt
import cv2 as cv

filename = os.path.join("..", "files", "26_04_2021_13:09:15_13:09:51.csv")
data = pd.read_csv(filename)

def denoise(res):

    # kernel = np.ones((5, 5), np.float32) / 25
    result = np.zeros(res.shape)
    # result = cv.fastNlMeansDenoising(res)
    dst = cv.fastNlMeansDenoisingColored(res, None, 10, 10, 7, 21)
    # plt.subplot(121), plt.imshow(matrix), plt.title('Original')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
    # plt.xticks([]), plt.yticks([])
    return result

def blur(matrix):

    kernel = np.ones((5, 5), np.float32) / 25
    dst = cv.filter2D(matrix, -1, kernel)
    return dst


# x = [20000, 20000, data.shape[0]]

matrix = np.zeros(shape=[1700, 1700, data.shape[0]], dtype=float, order='C')
matrix.fill(255)
for index, row in data.iterrows():
    for angle, value in enumerate(row[:-1]):
        x = int(value * math.cos(math.radians(angle))//10)+1000
        y = int(value * math.sin(math.radians(angle))//10)+1000
        # print(x, y)
        matrix[y, x, index] = 0

    # plt.figure(1)
    plt.subplot(221)
    plt.imshow(matrix[:, :, index], vmin=0, vmax=255, cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.subplot(222)
    res = blur(matrix[:, :, index])
    plt.imshow(res)
    plt.xticks([]), plt.yticks([])
    plt.subplot(223)
    res = blur(matrix[:, :, index])
    plt.imshow(res)
    plt.xticks([]), plt.yticks([])
    res = denoise(res)
    plt.imshow(res)
    plt.show()
    exit()
# print(matrix)
