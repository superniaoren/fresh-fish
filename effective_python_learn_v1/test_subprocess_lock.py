import os, sys, time, subprocess
import threading
from threading import Thread
from threading import Lock

class Counter(object):
    def __init__(self):
        self.count = 0
    
    def increment(self, value):
        self.count += value

class LockingCounter(object):
    def __init__(self):
        self.lock = Lock()
        self.count = 0
    def increment(self, value):
        #with self.lock:
        #    self.count += value
        if(self.lock.acquire()):
            self.count += value
            self.lock.release() 

def worker_cb(worker_idx, how_many, counter):
    for _ in range(how_many):
        # some read/load op
        # ...
        counter.increment(1)

def run_threads(cb_func, how_many, counter):
    threads = []
    for i in range(6):
        args = (i, how_many, counter)
        thread = Thread(target=cb_func, args=args)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()



if __name__ == '__main__':
    how_many = 10**5
    counter = Counter()
    run_threads(worker_cb, how_many, counter)
    print('Counter should be %d, real value %d' % (6 * how_many, counter.count))

    lock_counter = LockingCounter()
    run_threads(worker_cb, how_many, lock_counter)
    print('LockCounter should be %d, real value %d' % (6 * how_many, lock_counter.count))
