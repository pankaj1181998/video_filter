'''
 - Matplotlib 
'''

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

'''
Using fig = plt.figure() it is like manual method 
We have to set_axes , choose location ,size
Then plot
'''

'''
Second method is for subplots based on rows and columns .
Plot using row and columns .
Using we get array of 
'''
fig,axes = plt.subplots()
fig,axes = plt.subplots(nrows=1 ,ncols=2)

plt.tight_layout()

x = np.array([1.0,2.0,0.5,6.0,0.25])
y = np.array([1.0,2.0,3.0,0.2,0.5])

for current_ax in axes:
   current_ax.plot(x,y)

axes[0].set_title('First Plot')
axes[0].plot(y,x)
axes[1].set_title('Second Plot')
axes[1].plot(x,x)

'''
figure size , aspect ratio , dpi 
'''
#fig = plt.figure(figsize=(8,2),dpi=100) # dpi - pixels per inch , ppi
fig,ax = plt.subplots(nrows=2,ncols=1,figsize=(5,4)) # dpi - pixels per inch , ppi
ax[0].plot(x,y,label ='x|y')
ax[1].plot(y,x,label ='y/x')

ax[0].set_title('Third Plot')
ax[0].set_xlabel('X Axis')
ax[1].set_ylabel('Y axis')

ax[1].set_title('Third Plot')
ax[1].set_xlabel('X Axis')
ax[1].set_ylabel('Y axis')

ax[0].legend(loc=0)
ax[1].legend(loc=1)
'''
Location String	Location Code
'best'	0
'upper right'	1
'upper left'	2
'lower left'	3
'lower right'	4
'right'	5
'center left'	6
'center right'	7
'lower center'	8
'upper center'	9
'center'	10 
'''
plt.tight_layout()
fig.savefig('my_[icture.png',dpi=200)