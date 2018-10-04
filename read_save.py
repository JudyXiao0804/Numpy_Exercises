import numpy as np

arr = np.loadtxt('array_ex.txt', delimiter = ',')
print arr

arr = np.arange(10)
np.save('some_array', arr)
print np.load('some_array.npy')
print

np.savez('array_archive.npz', a = arr, b = arr)
arch = np.load('array_archive.npz')
print arch['b']
