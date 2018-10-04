# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print 'unique'
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

print np.unique(names)
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print np.unique(ints)
print

print 'in1d'
values = np.array([6, 0, 0, 3, 2, 5, 6])
print np.in1d(values, [2, 3, 6])
