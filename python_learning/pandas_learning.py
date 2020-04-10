'''
Pandas is open source library built on top of NumPy
It allows for fast analysis and data cleaning , preparation
It allows in performance and productivity
It also has built in visualization features
It can work with data from wide variety of resources . 

- Series
- DataFrames
- MissingData
- GroupBy
- Merging Joining and Concatenating 
- Operations
- Data Input & Output
'''

# Series (Similar to numpy arrays but has labels)

import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10 ,20,30]
arr = np.array(my_data)
d = { 'a':10 ,'b':20 ,'c':30}
print(pd.Series(data = my_data))
