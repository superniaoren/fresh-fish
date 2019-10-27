## priority queue: is a container data structure that manages 
## a set of records with totally-ordered keys to provide quick
## access to the record with the smallest or largest key in the set.

if __name__ == '__main__':
    print('test priority (key) queues: ')

    # list-based, maintaining a manually sorted queue
    # downside is that inserting new elements into a list is a slow O(n) operation.
    print('=' * 50)
    simple = []
    simple.append((4, '吕轻侯'))
    simple.append((0, '莫小贝'))
    simple.append((8, '白展堂'))
    # NOTE: remember to re-sort every time a new element is inserted, or  
    #       use bisect.insort()
    from bisect import insort, insort_right
    print('list-based priority queue: ', simple)
    simple.sort(reverse=True)
    sorted_simple = []
    #insort(sorted_simple, simple)
    #insort_right(sorted_simple, simple)
    print('list-based priority queue: ', sorted_simple)
    print('list-based priority queue: ', simple)

    while simple:
        #next_item = simple.pop(0)
        next_item = simple.pop()
        print('current popped: ', next_item)
    

    # heapq-based, list-based binary heaps
    # this is a binary heap implementation usually backed by a plain list,
    # and it supports insertion and extraction of the smallest element in O(log n) time
    import heapq
    print('=' * 50)
    heap = []
    heapq.heappush(heap, (9, '李秀莲'))
    heapq.heappush(heap, (3, '佟湘玉'))
    heapq.heappush(heap, (7, '郭芙蓉'))
    
    while heap:
        next_item = heapq.heappop(heap)
        print('heap popped: ', next_item)

    # queue-based, beautiful priority queues
    # this priority queue implementation uses heapq internally and 
    # shares the same time and space complexities.
    # DIFFERENCE is that PriorityQueue is synchronized and provides locking semantics to support multiple 
    # concurrent producers and consumers.
    from queue import PriorityQueue as PQ
    pq = PQ()
    pq.put((20, '六指轩辕'))
    pq.put((17, '燕小六'))
    pq.put((19, '邢捕头'))
    while not pq.empty():
        next_item = pq.get()
        print('PQ: ', next_item)
    
    
