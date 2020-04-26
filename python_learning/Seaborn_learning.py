'''
- Seaborn is a stastical plotting library
- It is build upon Matplotlib
- It has beautiful default styles
- It also is designed to work well with pandas dataframe
''' 

'''
    Distribution Plots
'''
import seaborn as sns

# seaborn comes with some builtin data sets
tips = sns.load_dataset('tips')
print(tips.head())