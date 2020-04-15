'''
Data Frames - Part 3 
'''

import pandas as pd
import numpy as np

from numpy.random import randn

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
# pd.DataFrame(data, index , columns)
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
# call from outside index to inside index
print(df.loc['G1'].loc[1])
# naming index

print(df.index.names)
df.index.names = ['Groups', 'Num']
print(df)

print(df.loc['G2'].loc[1])
print(df['A'])
print(df.loc['G2'].loc[1]['B'])

# xs - returns cross section of rows and columns
print(df.xs(1,level='Num'))