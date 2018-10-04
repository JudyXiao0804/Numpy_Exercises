# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random


print 'concatenate two arrays'
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
print np.concatenate([arr1, arr2], axis = 0)  # concatenating in row
print np.concatenate([arr1, arr2], axis = 1)  # concatenating in column
print


print 'vstack and hstack'
print np.vstack((arr1, arr2)) 
print np.hstack((arr1, arr2))

print 'splitting'
arr = np_random.randn(5, 5)
print arr

print 'splitting in rows'
first, second, third = np.split(arr, [1, 3], axis = 0)
print 'first'
print first
print 'second'
print second
print 'third'
print third

print 'splitting in columns'
first, second, third = np.split(arr, [1, 3], axis = 1)
print 'first'
print first
print 'second'
print second
print 'third'
print third
print


arr = np.arange(6)
arr1 = arr.reshape((3, 2))
arr2 = np_random.randn(3, 2)

print np.r_[arr1, arr2]

print np.c_[np.r_[arr1, arr2], arr]

print np.c_[1:6, -10:-5]
