# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print 'sum'
arr = np_random.randn(100)
print (arr > 0).sum()
print

print 'bools'
bools = np.array([False, False, True, False])
print bools.any() 
print bools.all() 
