from matplotlib import pyplot as plt
import numpy as np

mu, sigma = np.mean(CHT_array), np.std(CHT_array)
fig, ax = plt.subplots(figsize=(10,6))

x1 = [i*50 for i in range(21)]
#plt.figure(figsize=(10,6))
n, bins, patches = ax.hist(CHT_list, 
                            facecolor='blue', 
                            alpha=0.6,
                            density=1,
                            bins=x1)

y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')

plt.xlim(0, 1000)
plt.grid(True)
plt.xticks(x1)
ax.tick_params(axis="y", labelsize=20)
#plt.grid(axis='y', alpha=0.75)
fig.tight_layout()
plt.show()
