# -*- coding: utf-8 -*-

import numpy as np

arr = np.arange(8)
print arr.reshape((4, 2))
print arr.reshape((4, 2)).reshape((2, 4)) 
print

arr = np.arange(15)
print arr.reshape((5, -1))
print

other_arr = np.ones((3, 5))
print other_arr.shape
print arr.reshape(other_arr.shape)
print

arr = np.arange(15).reshape((5, 3))
print arr.ravel()
