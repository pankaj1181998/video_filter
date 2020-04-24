'''
    Data Input and Output - Pandas
    - CSV
    - HTML
    - Excel
    - SQL
    Libraries ( sqlalchemy , lxml , 
    html5lib , BeautifulSoup4 )
'''

import pandas as pd
import numpy as np


# Reading and Writing to CSV
print( pd.read_csv('example.csv'))

df = pd.DataFrame({
    'col1':[1,2,3,4],
    'col2':[444,555,666,444],
    'col3':['abc','def','ghi','xyz']
})
df.to_csv('My_Output',index = False)
print(pd.read_csv('My_output'))

pd.read_excel('example.xlsx',sheet_name='SalesOrders')
#print(pd.read_excel('example.xlsx',sheet_name='SalesOrders'))
df.to_excel('Excel_output.xlsx',sheet_name='NewSheet')
print(pd.read_excel('Excel_output.xlsx',sheet_name='NewSheet'))

data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
print(data[0])