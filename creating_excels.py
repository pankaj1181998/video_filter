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

def create_excel(file_name :str,mydict :dict):
   df = pd.DataFrame(mydict)
   df.to_excel('Report_File_Excels/'+ file_name +'.xlsx',sheet_name='Frames')
# print(pd.read_excel('Excel_output.xlsx',sheet_name='NewSheet'))
