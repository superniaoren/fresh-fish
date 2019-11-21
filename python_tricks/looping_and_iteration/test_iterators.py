## known as 'beautiful iterators'
##

# in the 1st naive examples, Repeater and RepeaterIterator work together
# it can be viewed as __iter__ and __next__ work together.
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
        self.counter += 1
        if self.counter < 10:
            #self.counter += 1
            print(self.counter)
            return self.source.value
        else:
            #self.counter += 1
            return self.counter
        # return None by default

class SingleRepeater:
    def __init__(self, value):
        self.value = value
   
    def __iter__(self):
        return self

    def __next__(self):
        return self.value

if __name__ == '__main__':
    print('learn iterators : ') 

    repeater = Repeater('Tatoon')
    # a infinite loop
    for item in repeater:
        print(item)
        break  # skip the endless loop

    # behind-scenes. Note the communications between repeater and Riterators:
    print('=' * 40)
    #iterator = repeater.__iter__()
    # OR:
    iterator = iter(repeater)
    while True:
        #item = iterator.__next__()
        # or: 
        item = next(iterator)
        print(item)
        break  # [zoo] for test

    
    repeater = SingleRepeater("Hayato")
    for item in repeater:
        print(item)
