'''
Merging , Joining , Concatenating 
'''
import pandas as pd
import numpy as np

df1 = pd.DataFrame(
    {'A': ['A0', 'A1', 'A2', 'A3'],
     'B': ['B0', 'B1', 'B2', 'B3'],
     'C': ['C0', 'C1', 'C2', 'C3'],
     'D': ['D0', 'D1', 'D2', 'D3']},
     index=[0, 1, 2, 3])

df2 = pd.DataFrame(
    {'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7']},
     index=[4, 5, 6, 7])
df3 = pd.DataFrame(
    {'A': ['A8', 'A9', 'A10', 'A11'],
     'B': ['B8', 'B9', 'B10', 'B11'],
     'C': ['C8', 'C9', 'C10', 'C11'],
     'D': ['D8', 'D9', 'D10', 'D11']},
     index=[8, 9, 10, 11])

# Concatenation should glues together data frames 
# Dimensions should match along the axis you are concatenating on .

print( pd.concat([df1,df2,df3])) 
# join along columns axis = 1 
print( pd.concat([df1,df2,df3],axis=1)) 


# Merge deone using key i.e on='key' , how - left ,right inner , outer
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(left,right,how='inner',on='key'))
print(pd.merge(left,right,how='left',on='key'))


left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])
# Join is a convinent method for combining two different indexed DataFrames into a single result DataFrame 

print( left.join(right) )
print( left.join(right,how='outer') )