## FIFOs

if __name__ == '__main__':
    print('test queuues: the code here is quite simple and naive.,', 
          'you can skip these test.')

    # list-based queue, terribly slow (O(n) time). [NOT Recommend]
    print('=' * 50)
    lqueue = []
    lqueue.append('white')
    lqueue.append('cook')
    lqueue.append('blue')
    print('list-based queue: ', lqueue)
    lqueue.pop(0)
    print('list-based queue: ', lqueue)
    lqueue.pop(0)
    print('list-based queue: ', lqueue)
    
    # dqueu-based queue, fast and robust
    from collections import deque
    print('=' * 50)
    dqueue = deque()
    dqueue.append('baid')
    dqueue.append('tesla')
    dqueue.append('huawei')
    print('dqueue-based queue: ', dqueue)
    dqueue.popleft()
    print('dqueue-based queue: ', dqueue)
    dqueue.popleft()
    print('dqueue-based queue: ', dqueue)
    
    # Queue-based queue: locking semantics for parallel computing
    # support multiple concurrent producers and consumers
    from queue import Queue
    print('=' * 50)
    baseq = Queue()
    baseq.put('brag')
    baseq.put('facemask')
    baseq.put('getoutofhere')
    print('Queue-based queue: ', baseq)
    print('Queue-based queue: ', baseq.get())
    print('Queue-based queue: ', baseq.get())
    print('Queue-based queue: ', baseq.get())

    # mutliprocessing queue, shared job queues
    # allow queuedj items to be processed in parallel by multiple concurrent
    # workers. Process-based parallelization is popular in CPython due to 
    # the global interpreter lock(GIL) that prevent parallel executon on a 
    # single interpreter process.
    # mutliprocessing.Queue work around the GIL limitations.
    # This type of queue can store and transfer any pickle-able object across
    # process boundaries.
    from multiprocessing import Queue as mQueue
    print('=' * 50)
    mqueue = mQueue()
    mqueue.put('moxiao')
    mqueue.put('grab')
    mqueue.put('bangkok')
    print('multiprocessing Queue-based: ', mqueue)
    mqueue.get()
    print('multiprocessing Queue-based: ', mqueue)
    print('multiprocessing Queue-based: ', mqueue.get())
    print('multiprocessing Queue-based: ', mqueue.get())
    # if mqueue is empty, get() would blocks the current process and wait 
    #print('multiprocessing Queue-based: ', mqueue.get())
    
