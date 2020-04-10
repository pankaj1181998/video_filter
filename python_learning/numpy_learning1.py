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

print(arr[3])
print(arr[1:4])
print(arr[0:5])
print(arr[5:])
arr[0:5]=100
print(arr)

# numpy doesn't make a copy own it's own

slice_of_arr = arr[0:6]
print()

# To make the copy of an array 	
arr_copy = arr.copy()

arr_2d = np.array([[3,2,1,5],[9,6,3,4],[0,4,7,8]])
print(arr_2d[1][1])
print(arr_2d[1,1])
print(arr_2d[:2,1:])
print(arr_2d[:2])

arr = np.arange(1,11)
print (arr > 5) 
bool_arr = arr > 5
print(bool_arr)

print(arr[arr<8])

arr_2dd = np.arange(50).reshape(5,10)
print(arr_2dd)

print(arr_2dd[1:3,1:6])
