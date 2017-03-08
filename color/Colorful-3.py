
# 1 - 100無顏色變化
from __future__ import print_function
for i in range(1,1000):
     print('\033[38;5;{:>3}m{:>3}\033[0m  '.format(str(i),str(i)),end='')
     if (i%10) == 0:
         print('')
