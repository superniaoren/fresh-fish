##
import os, sys, time, subprocess

import threading
from threading import Thread
from threading import Lock

import collections
from collections import deque

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
