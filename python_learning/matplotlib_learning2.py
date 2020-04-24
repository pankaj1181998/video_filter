'''
Matlplot Learning 3 
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = x * 2
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
# linewidth or lw | linestyle or ls
# also can put RGB hex codes for more colors
# apha for line transparency
ax.plot(x,y,color='green' , linewidth = 5 ,alpha = 0.5 , linestyle='--') 

#marking all elements or points

ax.plot(x,y,color='green' , lw = 5 ,alpha = 0.5 , ls='--' , marker='o' ,
        markerfacecolor='yellow',markeredgewidth=3, markersize=20) 

