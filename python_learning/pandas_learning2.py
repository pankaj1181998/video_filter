import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

# condition selection
print (df > 0)
booldf = df>0
# to get true result
print(df[booldf])
print()
#return boolean answer
print(df[df>0])
print()

print(df)
# will return series of w
print(df['W']>0)

# only return rows which are greater than zero
# C won't be printed 
print(df[df['W']>0])
print(df [df['Z'] <0])

resultdf = df[df['W']>0]
print(resultdf['X'])

print(df[df['W']>0]['X'])

print(df[df['W']>0][['X','Y']])
   
# Implementation
boolser = df['W']>0
result = df[boolser]
mycols = ['Y','X']
result[mycols]

# Will Throw an Error
# df[(df['W']>0) and (df['Y']>1)]
print ( df[(df['W']>0) & (df['Y']>1)])
print ( df[(df['W']>0) | (df['Y']>1)])

# SET_INDEX VS RESET_INDEX
print( df.reset_index() )
newind = 'CA NY WY OR CO'.split()
print(newind)
df['States'] = newind
print(df.set_index('States'))

