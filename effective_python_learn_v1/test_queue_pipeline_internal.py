import sys, os, time
from queue import Queue

import threading
from threading import Thread
#from threading import Lock

# set the queue buffer size 1
# the putting and getting interleaved
#queue = Queue()
queue = Queue(1)
work_count = 0
job_num = 10

def consume():
    global work_count
    while True: 
        queue.get()
        print('consumer get waiting 1')
        work_count += 1
        if work_count >= job_num:
            queue.task_done()
            break
    #queue.get()
    #print('consumer get waiting 2')

    #  
    #print('consumer done')
    #queue.task_done()

# Queue.task_done() + Queue.join()

thread = Thread(target=consume)
thread.start()

for i in range(job_num):
    queue.put(object())
    print('producer putting ', i)

# [TODO] why the queue.join() block the procedure ?
#queue.join()

#thread.join()
print('producer done')
