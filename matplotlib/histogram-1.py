from matplotlib import pyplot as plt
import numpy as np

x1 = [i*50 for i in range(21)]
plt.figure(figsize=(10,6))
n, bins, patches = plt.hist(CHT_list, 
                            facecolor='blue', 
                            alpha=0.6,
                            bins=x1)

plt.xlim(0, 1000)

plt.grid(True)
plt.xticks(x1)


plt.show()
