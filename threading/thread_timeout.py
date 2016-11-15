#!/mnt/ext/opt/Python/bin/python
# 利用thread將執行過久的process終止，並輸出執行結果

import subprocess
import threading

class Command():
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
            print 'Thread started'
            self.process = subprocess.Popen(self.cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            self.res, err = self.process.communicate()
        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            print 'Terminating process'
            self.process.terminate()
            thread.join()
        print self.process.returncode

command = Command("ping 8.8.8.8 -c 10")
command.run(timeout = 3)
print "This is result: ",command.res
