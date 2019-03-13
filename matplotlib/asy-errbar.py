import numpy as np
import matplotlib.pyplot as plt
# demo matplotlib asymmetric Error Bars
# ref: https://matplotlib.org/2.0.0/api/_as_gen/matplotlib.axes.Axes.errorbar.html

x  = [i for i in range(6)]
y  = [i for i in range(10,16)]
y1 = [i for i in range(20,26)]

fig, ax = plt.subplots(figsize=(12, 4))

ax.errorbar(x,
            y,
            yerr=[[1,2,3,4,5,6],[1,1,1,1,1,1]],
            ecolor='c',    # color of error bar
            label='first',
           )

ax.errorbar(x,
            y1,
            yerr=[[1,2,3,4,5,6],[1,1,1,1,1,1]],
            ecolor='b',    # color of error bar
            label='second',
           )

ax.legend()
ax.grid()

ax.set_title('MD-LOST')
labels = ['a','b','c','d','e','f']
plt.xticks(x, labels)
plt.savefig('0919.png')

