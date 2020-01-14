#!/usr/bin/python3
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker as ticker
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime

data = pd.read_csv('123.txt', sep=',', header=None)
data = data.rename(columns={0:'Time',1:'Price'})
#data = data.set_index('Time')
x = data['Time']
xx = []
# 2013-01-01 00:50:18
for i in x:
    print(i)
    tmp = datetime.strptime(str(i), "%Y-%m-%d %H:%M:%S")
    xx.append(tmp)

y = data['Price']
#hours   = mdates.HourLocator()
minutes = mdates.MinuteLocator()
seconds1 = mdates.SecondLocator()
seconds2 = mdates.SecondLocator(interval=5)

fig, ax = plt.subplots()
fig.set_figheight(15)
fig.set_figwidth(15)
ax.plot(xx,y, 'go-')

ax.xaxis.set_major_locator(seconds2)
ax.xaxis.set_minor_locator(seconds1)
dateFmt = mdates.DateFormatter('%M:%S')
ax.xaxis.set_major_formatter(dateFmt)

##plt.show()
#
plt.grid()
plt.xticks(rotation=45)
