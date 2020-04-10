'''
NumPy is the fundamental package for scientific computing with Python. It contains among other things:
	- a powerful N-dimensional array object
	- sophisticated (broadcasting) functions
	- tools for integrating C/C++ and Fortran code
	- useful linear algebra, Fourier transform, and random number capabilities
'''

import numpy as np
arr = np.arange(0,11)
print(arr)
# Addition & Substraction of arr
print(arr + arr)
print(arr - arr)

# Scalar Operation on Array
print(arr-100)

# exponent
print (arr ** 2)

#Square Root , Power  , Log , Exponential 
print(np.sqrt(arr))
print(np.exp(arr))
print(np.max(arr))
print(np.sin(arr))
print(np.log(arr))