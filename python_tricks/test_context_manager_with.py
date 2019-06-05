import os
import sys
import contextlib


#class Indent(object):
class Indent:
    def __init__(self):
        self.level = 0
    
    def __enter__(self):
        self.level += 4
        return self.level

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 4
        
    def print(self, text):
        #print('-' * self.level + text)
        print('-' * self.level)
        


if __name__ == '__main__':
    print('test %s '% os.__file__)
    with Indent() as indent:
        #indent.print('ok, ok, sudongpo')
        indent.print('ok')
        with indent:
            indent.print('again, see the indent chars')
            with indent:
                indent.print('flowers are all dead')
        indent.print('Here')
    
