# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random
from random import normalvariate

print 'random sample of normal distribution'
samples = np.random.normal(size=(4, 4))
print samples

print 'random sample between 0 and 1 obeying normal distribution'
N = 10
print [normalvariate(0, 1) for _ in xrange(N)]
print np.random.normal(size = N)  
