'''
GROUPBY - Pandas
 - Groupby allows you to group together rows based off of a column and perform an aggregate dunction on them
'''
import pandas as pd
import numpy as np
data = {
        'Company' :['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person' :['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales' :[200,120,340,124,243,350]
        }
df = pd.DataFrame(data)
print(df)

print(df.groupby('Company'))
byComp = df.groupby('Company')
# byComp will refer to an address
print(byComp.mean()) # Will give mean for sales comlumn and ignores non-numeric columns
print(byComp.sum())
print(byComp.std()) # standard deviation - std
print()
print(byComp.sum().loc['FB'])

# All functions in one  
print(df.groupby('Company').count())
print(df.groupby('Company').max ()) # Max and min for string returns alphabetically

# describe shows main elements  
print(df.groupby('Company').describe())
print(df.groupby('Company').describe().transpose())
print(df.groupby('Company').describe().transpose()['FB'])

