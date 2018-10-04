# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

arr = np_random.randn(8)
arr.sort()
print arr
print

arr = np_random.randn(5, 3)
print arr
arr.sort(1) 
print arr


large_arr = np_random.randn(1000)
large_arr.sort()
print large_arr[int(0.05 * len(large_arr))]
