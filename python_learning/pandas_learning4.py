'''
Pandas - Missing Data
'''

import numpy as np
import pandas as pd

# np.nan - NULL / Missing value in pandas
d = {'A':[1,2,np.nan] , 'B':[5,np.nan,np.nan] , 'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)

#drops row if it has null value
print(df.dropna())
print(df.dropna(axis=1)) # drops columns if null is there
print(df.dropna(thresh=2)) # drops if there atleast thresh non Na values

#filling na/null values
print( df.fillna(value='FILL VALUE'))
print( df.fillna(value=df['A'].mean()))
