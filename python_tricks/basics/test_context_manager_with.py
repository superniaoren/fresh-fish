import os
import sys
import time
import contextlib
from contextlib import contextmanager


# context management template
class CtxManage(object):
    def __init__(self):
        print('init the context manager:')
    
    def __enter__(self):
        print('enter the context manager:')
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit the context manager.')

#class Indent:
class Indent(object):
    def __init__(self):
        self.level = 0
    
    def __enter__(self):
        self.level += 4
        #return self.level  # error
        return self

    #def __exit__(self, exc_type, exc_val, exc_tb):
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.level -= 4
        
    def print(self, text):
        print('-' * self.level + text)
        #print('-' * self.level)

@contextmanager
def CtxFileMange(filename):
    try:
        fh = open(filename, 'w')
        yield fh
    finally:
        fh.close()

class CtxFileMange_2(object):
    def __init__(self, filename, mode):
        self.file = None
        self.name = filename
        self.mode = mode

    def __enter__(self):
        '''
        try:
            self.file = open(self.name, self.mode)
        except ValueError:
            print('fail to open file %s' % self.name)
            exit(1)
        '''
        self.file = open(self.name, self.mode)
        return self.file
 
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        
# generator based
@contextmanager
def CtxTimer(tags=None):
    try:
        start = time.time()
        # do some stuff:
        # block by yield
        yield tags
    finally:
        print(tags)
        stop = time.time()
        elapsed = (stop - start) * 1000.0 # ms
        print('elpased time: %4.0f ms' % elapsed)
    
# class based
class CtxTimer_2(object):
    def __init__(self):
        self.elpased = 0.
        self.start = 0.
        self.stop = 0.

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb): 
        self.stop = time.time()
        self.elapsed = (self.stop - self.start) * 1000.0
        print('elpased time: %4.0f ms' % self.elapsed)
        


if __name__ == '__main__':
    print('test %s '% os.__file__)

    with CtxManage() as cm:
        print('with block of ctx-manage')

    with Indent() as indent:
        #indent.printer('ok, ok, sudongpo')
        indent.print('ok')
        with indent:
            indent.print('again, see the indent chars')
            with indent:
                indent.print('flowers are all dead')
        indent.print('Here')
        print('here')
    

    with CtxFileMange('./ctx_filemange.txt') as f:
        f.write('mengmeng.cat\n')
        f.write('maomao.dog\n')

    with CtxFileMange_2('./ctx_filename_2.txt', 'w') as f:
        f.write('xuehua.cat\n')
        f.write('daidai.cat\n')


    with CtxTimer(tags={'zoo': 'timer'}) as ct:
        ct['fast'] = 'zero'
        time.sleep(1)
    
    with CtxTimer_2() as ct:
        print('do some stuff here')
        time.sleep(1)



