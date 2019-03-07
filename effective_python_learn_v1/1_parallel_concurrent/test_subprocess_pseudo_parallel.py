import os, sys, time, subprocess
from threading import Thread

import select

## sequential computation, async/parallel I/O operation.

def pseudo_io():
    select.select([], [], [], 0.1)  # 0.1s

def factorize(num):
    for i in range(1, num + 1):
        if num % i == 0:
            yield i

class factorizeThread(Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num 
    def run(self):
        self.factors = list(factorize(self.num))

if __name__ == '__main__':
    nums = []
    for _ in range(5):
        rand = os.urandom(100000)
        nums.append(rand)
    
    nums = [123422, 1341, 15563567]
    
    print("(default) Sequential mode:")
    start = time.time()
    for num in nums:
        list(factorize(num))
    
    end = time.time()
    
    print("sequential: time elapsed %.3f seconds" % (end - start))

    print("(pseudo) Trheading mode:")
    start = time.time()
    threads = []
    for num in nums:
        thread = factorizeThread(num)
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    end = time.time()
    print("threading: time elapsed %.3f seconds" % (end - start))

    print("(pseudo) blocking IO mode:")
    start = time.time()
    for _ in range(3):
        pseudo_io()
    end = time.time()
    print("pseudo io: time elapsed %.3f seconds" % (end - start))

    print("(async) blocking IO mode:")
    start = time.time()
    threads = []
    for _ in range(3):
        thread = Thread(target=pseudo_io)
        #threads.append(thread)
        thread.start()
        threads.append(thread)
        ## TODO: the computtion logic
    for thread in threads:
            thread.join()
    end = time.time()
    print("async io: time elapsed %.3f seconds" % (end - start))
