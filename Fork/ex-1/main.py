#!/usr/bin/python3
import os
parm = 0
while True:
    parm += 1
    pid = os.fork()
    if pid == 0:
# copy process
        os.execlp('python','python', 'echo.py', str(parm)) # overlay program
        assert False, 'error starting program'
# shouldn't return
    else:
        print('Child is', pid)
        if input() == 'q': break
