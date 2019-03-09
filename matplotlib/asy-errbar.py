import numpy as np
import matplotlib.pyplot as plt
# demo matplotlib asymmetric Error Bars

x = [i for i in range(6)]
y = [i for i in range(10,16)]

fig, ax = plt.subplots(figsize=(12, 4))

ax.errorbar(x,
            y,
            yerr=[[1,2,3,4,5,6],[1,1,1,1,1,1]],
            ecolor='c',    # color of error bar
           )

ax.set_title('MD-LOST')
labels = ['a','b','c','d','e','f']
plt.xticks(x, labels)
plt.savefig('0919.png')
