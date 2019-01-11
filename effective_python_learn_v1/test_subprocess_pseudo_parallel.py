import os, sys, time, subprocess
from threading import Thread

## sequential computation, async/parallel I/O operation.

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
