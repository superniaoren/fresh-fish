import os, sys
import time

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return -1
    
if __name__ == '__main__':
    numbers = [(1537, 2256379), (177777, 199995), 
               (147858, 498425), (542301, 598119)]
    
    start = time.time()
    results = list(map(gcd, numbers))
    stop  = time.time()
     
    print('results = {}'.format(results))
    print('single cpu thread time cost: %.3f secs' % (stop - start))

    fake_pool = ThreadPoolExecutor(max_workers=4)
    start = time.time()
    results = list(fake_pool.map(gcd, numbers))
    stop  = time.time()
     
    print('results = {}'.format(results))
    print('fake multi-threads time cost: %.3f secs' % (stop - start))

    true_pool = ProcessPoolExecutor(max_workers=4)
    start = time.time()
    results = list(true_pool.map(gcd, numbers))
    stop  = time.time()
     
    print('results = {}'.format(results))
    print('true multi-processes time cost: %.3f secs' % (stop - start))

