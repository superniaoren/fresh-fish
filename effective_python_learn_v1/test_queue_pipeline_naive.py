##
import os, sys, time, subprocess

import threading
from threading import Thread
from threading import Lock

import collections
from collections import deque

from queue import Queue

class myQueue(object):
    def __init__(self):
        self.items = deque()
        self.lock = Lock()


    def put(self, item):
        with self.lock:
            self.items.append(item)

    def get(self):
        with self.lock:
            return self.items.popleft()

class worker(Thread):
    def __init__(self, job_num, fn_cb, in_queue, out_queue):
        super().__init__()
        self.func = fn_cb
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

    def run(self):
        while True and self.work_done < job_num:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                #print("met IndexError")
                time.sleep(0.01)
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.work_done += 1

def download(object):
    print('download object')

def resize(object):
    print('resize object')
    
def upload(object):
    print('upload object')


if __name__ == '__main__':
    job_num = 20
    # naive pipeline 
    download_queue = myQueue()
    resize_queue = myQueue()
    upload_queue = myQueue()
    done_queue   = myQueue()
    threads = [
        worker(job_num, download, download_queue, resize_queue),
        worker(job_num, resize, resize_queue, upload_queue),
        worker(job_num, upload, upload_queue, done_queue)
    ]
    
    for thread in threads:
        thread.start()

    for _ in range(job_num):
        download_queue.put(object())

    while (len(done_queue.items)) < job_num:
        # waiting 
        curr_done_queue_count = len(done_queue.items)
        print('curr done queue count ', curr_done_queue_count)
        time.sleep(0.01)
    else:
        done_queue_count = len(done_queue.items)
        total_polled_count = sum(t.polled_count for t in threads)
        total_work_done = sum(t.work_done for t in threads)
        print("done queue count ", done_queue_count, \
              " polled count ", total_polled_count,  \
              " work done count ", total_work_done)
        for thread in threads:
            thread.join()

