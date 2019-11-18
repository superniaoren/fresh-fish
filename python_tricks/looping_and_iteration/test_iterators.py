## known as 'beautiful iterators'
##

class Repeater:
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        return RepeaterIterator(self)

class RepeaterIterator:
    def __init__(self, source):
        self.source = source
        self.counter = 0

    def __next__(self):
        if self.counter < 10:
            #self.counter += 1
            print(self.counter)
            return self.source.value
        else:
            self.counter += 1

if __name__ == '__main__':
    print('learn iterators : ') 

    repeater = Repeater('Tatoon')
    for item in repeater:
        print(item)

