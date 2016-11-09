#!/usr/bin/python2
import os
import sys

child_pid = os.fork()
if child_pid == 0:
    print("THIS is CHILD")
    sys.exit(0)

pid, status = os.waitpid(child_pid, 0)   # 第二個是option
print("THIS is pid: {}, status: {}".format(pid, status))


-------------------------------------------
option:
linux中只支持 WHNOHANG 和 WUNTRACED
#define WNOHANG        1
#define WUNTRACED      2
如果使用了WNOHANG参数调用waitpid，即使没有子进程退出，
它也会立即返回，不会像wait那样永远等下去

如果我们不想使用它们，也可以把options设为0，如： 　　
        ret=waitpid(-1,NULL,0); 　<---- 這應該是C的code
    
