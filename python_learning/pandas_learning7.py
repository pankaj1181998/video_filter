'''
Operations - pandas
'''

import pandas as pd
import numpy as np
df = pd.DataFrame({
    'col1':[1,2,3,4],
    'col2':[444,555,666,444],
    'col3':['abc','def','ghi','xyz']
})
print (df.head())
# Unique Values in dataFrames

print( df['col2'].unique() )
print( df['col2'].nunique() ) # Total returns of unique or lenght of array
print(len(df['col2'].unique())) # total unique values

print(df['col2'].value_counts()) # Times unique values come in data
print(df[df['col1'] > 2])
print()
print( ( df[ (df['col1'] > 2) & (df['col2'] == 444)] ))

def times2(x):
   return x*2 
 
print (df['col1'].apply(times2))
print (df.drop('col1',axis=1))
print(df.index)

print( df.sort_values(by='col2'))
print( df.isnull())

#print(df.pivot_table(values='col3',index=['col1','col2'],columns=['col1']))