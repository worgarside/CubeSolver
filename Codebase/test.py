#!/usr/bin/python3

import queue
import threading
import datetime
import time

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, q, func):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.q = q
        self.func = func

    def run(self):
        print("Starting " + self.name)
        self.func(self.q)
        print("Exiting " + self.name)


def create_data(q):
    while True:
        q.put(str(datetime.datetime.now().time()))
        time.sleep(0.5)

def print_data(q):
    time.sleep(10)
    while not q.empty():
        data = q.get()
        print(data)

# queueLock = threading.Lock()
workQueue = queue.Queue(0)

# Create new threads
# for tName in threadList:
#     thread = MyThread(threadID, tName, workQueue)
#     thread.start()
#     threads.append(thread)
#     threadID += 1

gen_thread = MyThread(1, 'gen', workQueue, create_data)
print_thread = MyThread(2, 'print', workQueue, print_data)

gen_thread.start()
print_thread.start()

gen_thread.join()
print_thread.join()

print("Exiting Main Thread")
