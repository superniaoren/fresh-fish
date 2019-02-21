import sys, os, time
from queue import Queue

import threading
from threading import Thread
#from threading import Lock

class closeQueue(Queue):
    CLOSE_SIG = object()
    
    def close(self):
        self.put(self.CLOSE_SIG)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.CLOSE_SIG:
                    return  # exit the iteration
                yield item
            finally:
                self.task_done()

class stopWorker(Thread):
    def __init__(self, func_cb, in_queue, out_queue):
        print('init the stopWorker class')
        super().__init__()
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.func = func_cb

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)


def download(object):
    print('execute download function')

def resize(object):
    print('execute resize function')

download_queue = closeQueue()
resize_queue = closeQueue()
done_queue = closeQueue()

threads = [
            stopWorker(download, download_queue, resize_queue),
            stopWorker(resize, resize_queue, done_queue),
        ]

for thread in threads:
    thread.start()
    
for _ in range(10):
    download_queue.put(object())

# close itself !
download_queue.close()
# join: wait to be consumed by the consumer queue 
download_queue.join()

resize_queue.close()
resize_queue.join()

done_queue.close()
#done_queue.join()
print(done_queue.qsize(), 'items closed ')
