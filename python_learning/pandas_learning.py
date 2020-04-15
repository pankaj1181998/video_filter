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

'''
Series (Similar to numpy arrays but has labels)
'''
import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10 ,20,30]
arr = np.array(my_data)
d = { 'a':10 ,'b':20 ,'c':30}
print(pd.Series(data = my_data))
print(pd.Series(data=my_data , index = labels))
print(pd.Series(my_data,labels))
print(pd.Series(arr,labels))
print("DIctionaries")
print(pd.Series(d))
print(pd.Series(data=labels))
print("Seriies can hold reference to functions")
print(pd.Series(data=[sum,print,len]))

print("-------------------------------")
ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
print(ser1)
print("---------")
ser2 = pd.Series([1,2,3,4],['USA','Germany','Italy','Japan'])  
print(ser2)
ser3 = pd.Series(data=labels)
#ingeter gets convert to float while doing operations
print(ser1 + ser2)
