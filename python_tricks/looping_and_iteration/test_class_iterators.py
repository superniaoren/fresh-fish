## known as 'beautiful iterators'
##

# in the 1st naive examples, Repeater and RepeaterIterator work together
# it can be viewed as __iter__ and __next__ work together.
class TwoPhaseRepeater:
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        return TwoPhaseRepeaterIterator(self)

class TwoPhaseRepeaterIterator:
    def __init__(self, source):
        self.source = source
        self.counter = 0
        self.max_repeats = 10

    def __next__(self):
        self.counter += 1
        if self.counter > self.max_repeats:
            print(self.counter)
            raise StopIteration  # use raise, not return
        else:
            return self.counter
        # return None by default

class SingleRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.counter = 0
   
    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.max_repeats:
            raise StopIteration
        self.counter += 1
        return self.value

if __name__ == '__main__':
    print('learn iterators : ') 

    repeater = TwoPhaseRepeater('TwoPhase: Tatoon')
    # a infinite loop
    for item in repeater:
        print(item)
        #break  # skip the endless loop

    # behind-scenes. Note the communications between repeater and Riterators:
    print('=' * 40)
    #iterator = repeater.__iter__()
    # OR:
    iterator = iter(repeater)
    while True:
        #item = iterator.__next__()
        # or: 
        try:
            item = next(iterator)
            #print(item)
        except StopIteration:
            break
        print(item)

    print('=' * 40)
    repeater = SingleRepeater("Single: Hayato", 5)
    #for item in repeater:
    #    print(item)
    while True:
        try:
            item = next(repeater)
        except StopIteration:
            break
        print(item)
