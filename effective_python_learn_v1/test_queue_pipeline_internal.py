import sys, os, time
from queue import Queue

import threading
from threading import Thread
#from threading import Lock

# set the queue buffer size 1
# the putting and getting interleaved
#queue = Queue()
queue = Queue(1)

def consume():
    time.sleep(0.01)
    queue.get()
    print('consumer get waiting 1')
    queue.get()
    print('consumer get waiting 2')
    #print('consumer done')

thread = Thread(target=consume)
thread.start()

queue.put(object())
print('producer putting 1')
queue.put(object())
print('producer putting 2')

thread.join()
print('producer done')
