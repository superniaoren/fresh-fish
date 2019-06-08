import os
import sys
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


