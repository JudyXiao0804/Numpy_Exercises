# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print 'square'
arr = np.arange(10)
print np.sqrt(arr)
print

print 'comparison'
x = np_random.randn(8)
y = np_random.randn(8)
print x
print y
print np.maximum(x, y)
print

print 'divide into inter and float'
arr = np_random.randn(7) * 5  # 统一乘5
print np.modf(arr)
