#!/usr/bin/python3

import threading, time
count = 0

def adder(addlock):
    global count
    with addlock:
        count = count + 1
    time.sleep(0.5)
    with addlock:
        count = count + 1

addlock = threading.Lock()
threads = []

for i in range(100):  # 從這裡一個一個塞進去
    thread = threading.Thread(target=adder, args=(addlock,))
    thread.start()
    threads.append(thread)

for thread in threads: # 在這邊等全部執行完畢
    thread.join()

print(count)
