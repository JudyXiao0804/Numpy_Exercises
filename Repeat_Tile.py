# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print 'Repeat'
arr = np.arange(4)
print arr.repeat(4)
print arr.repeat([1,2, 3, 4])
print

print 'Repeat in row or column'
arr = np_random.randn(2, 2)
print arr
print arr.repeat(2, axis = 0) # repeat in row
print arr.repeat(2, axis = 1) # repeat in column
print

print 'Tile'
print np.tile(arr, 2)
print np.tile(arr, (2, 3)) 
