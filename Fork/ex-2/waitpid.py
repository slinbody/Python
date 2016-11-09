#!/usr/bin/python2
import os
import sys

child_pid = os.fork()
if child_pid == 0:
    print("THIS is CHILD")
    sys.exit(0)

pid, status = os.waitpid(child_pid, 0)
print("THIS is pid: {}, status: {}".format(pid, status))
