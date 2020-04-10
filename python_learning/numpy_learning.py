'''
NumPy is the fundamental package for scientific computing with Python. It contains among other things:
	- a powerful N-dimensional array object
	- sophisticated (broadcasting) functions
	- tools for integrating C/C++ and Fortran code
	- useful linear algebra, Fourier transform, and random number capabilities
'''

import numpy as np

# Created a List Array 
my_list  = [1,2,3,4,5]

# passing List to numpy Array 
np_arr = np.array(my_list)
print(np_arr)

my_mat=[[1,2,3],[5,6,7],[3,5,3]]
np_arr1 = np.array(my_mat)
print(np_arr1)

 # Rangess in numpy
 print("Ranges in Numpy")
print( np.arange(0,5) )  # arange - Single R
print(np.arange(1,11,2)) # 3rd argument for differences

# zero vectors and arrays
print(np.zeros(5))
print(np.zeros((4,5)))

# Ones vectors and arrays
print(np.ones(4))
print(np.ones((4,5))) 

#linspace plots point at equal distance between range
print(np.linspace(0,5,4))
print(np.eye(4))

# Random generation of numbers
print(np.random.rand(4,4))

# To return from standard or gausian distribtion
print( np.random.randn(2) )
print( np.random.randn(3,3) )

# Returns number from low to high end
print("randint--------")
randarr = np.random.randint(0,50,10)
print("randarr")
print( randarr )
print("Reshaped Randarr")
print(randarr.reshape(2,5))

# maximum and minimum in vector / matrix
print(randarr.max())
print(randarr.min())
print(randarr.argmax())
print(randarr.argmin())

# Returns row , column 
print(randarr.shape)

# Reshaping arr
randarr = randarr.reshape(5,2)

print(randarr)
print(randarr.dtype)