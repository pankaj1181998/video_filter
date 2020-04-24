'''
 - Matplotlib is most popular plotting library .
 - It gives you control over every aspect of a figure .
 - It was designed to have a similar feel to MatLab's graphical plotting
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

plt.plot(x,y)
plt.plot(x,y,'r-') # Make color red
plt.xlabel('X label')
plt.ylabel('Y Label')
plt.title('Title')
# plt.show()

# Creating Multiplot on Same 

plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')

# plt.show()

## Object Oriented
fig = plt.figure()

#axes = fig.add_axes([0.1,0.1,0.8,0.8])
#axes1.plot(x,y,'g')
#axes.set_title('Axes')
#axes.set_xlabel('X Label')
#axes.set_ylabel('Y Label')

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
# add_axes(distance from left, distance from bottom , width of canvas , length of canvas )
axes1.plot(y,x)
axes2.plot(x,y)

