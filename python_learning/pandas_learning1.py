'''
Data Frames 

Data Frames is list of series in pandas
'''
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame( randn(5,4),['A','B','C','D','E'],['W','X','Y','Z']) 
print(df)

# printing and selecting columns
print(df['W'])
print(type(df))
print(df.W )
print( df[['W','Z']])

# creating a new column
#df['new']  --> will throw an error
df['new'] = df['W']+df['Y']
print(df)
#removing column 

# df.drop(new)   --> will throw an error
df.drop('new',axis=1,inplace=True)
# or df = df.drop('new',axis=1)
df.drop('E',axis=0,inplace=True)
print(df)

print(df.shape)

# Selecting/print ROws
print( df.loc['A'] )
print( df.iloc[2])

# selecting/printing subset  row,column 
print ( df.loc[ ['A','B'],['W','Y'] ] )