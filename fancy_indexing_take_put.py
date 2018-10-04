# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print 'Fancy Indexing example'
arr = np.arange(10) * 100
inds = [7, 1, 2, 6]
print arr[inds]
print

print 'using take'
print arr.take(inds)
print

print 'using put for update'
arr.put(inds, 50)
print arr
arr.put(inds, [70, 10, 20, 60])
print arr
print

print 'take'
arr = np_random.randn(2, 4)
inds = [2, 0, 2, 1]
print arr
print arr.take(inds, axis = 1)  
