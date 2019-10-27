##  stacks LIFO: last in, first out
##

if __name__ == '__main__':
    print('last in, first out: ')

    # list: simple, built-in stacks
    # [drawbacks]: python's lists are implemented as dynamic arrays internally, which means 
    #              they occasionally need to resize the storage space for elements stored 
    #              in them when elements are added or removed, which make their performance
    #              less consistent than the stable O(1) inserts and deletes provied by 
    #              a linked list based implementation.
    print('=' * 50)
    simple = []
    print('type: ', type(simple))
    simple.append('emotions')
    simple.append('injury')
    simple.append('insult')
    print('list-based stack: ', simple)
    simple.pop()
    simple.pop()
    print('list-based stack: ', simple)

    # deque: double end queue, fast & robust stacks
    # note, because support adding and removing elements from either end equally well, they 
    # can serve both as queues and as stacks.
    print('=' * 50)
    from collections import deque
    dacks = deque()
    dacks.append('song')
    dacks.append('south')
    dacks.append('kiring')
    print('deque-based stack: ', dacks)
    dacks.pop()
    print('deque-based stack: ', dacks)
    dacks.pop()
    print('deque-based stack: ', dacks)

    # LifoQueue: locking semantics for parallel computing
    # this stack implementation is synchronized and provides locking to support 
    # multiple concurrent producers and consumers. 
    print('=' * 50)
    from queue import LifoQueue as lq
    lacks = lq()
    lacks.put('tong')
    lacks.put('lao-bai')
    lacks.put('heng-mountain')
    print('LifoQueue-based stack: ', lacks)
    lacks.get()
    print('LifoQueue-based stack: ', lacks)
    lacks.get_nowait()
    print('LifoQueue-based stack: ', lacks)
    
    print('LifoQueue-based stack: ', lacks.get())
