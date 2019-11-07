## 
## Python yield is confusing. It's always tied to Python genertor
## https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
## USEFUL: yield is not as magical this answer suggests. When you call a function that 
##         contains a yield statement anywhere, you get a generator object, but no code runs.
##         Then each time you extract an object from the generator, Python executes 
##         code in the function until it comes to a yield statement, then pauses and 
##         delivers the object. When you extract another object, Python resumes just 
##         after the yield and continues until it reaches another yield 
##         (often the same one, but one iteration later). This continues until the 
##         function runs off the end, at which point the generator is deemed exhausted.

if __name__ == '__main__':
    print('review and learn yield again: ')
    print('to understand what `yield` is, U should first understand what `generator` is. ') 
    # for example, create an iterable var:
    print('=' * 50)
    mylist = [x * x for x in range(5)]
    print('type of mylist: ', type(mylist))
    for i in mylist:
        print(i)
    # here  mylist is an iterable. everything you can use 'for ... in ...' on is an iterable.
    # these iterables are handy cause you can read them as much as you wish,
    # BUT you store all the values in memory and this is not always you want when you have 
    # a lot of values.

    # generators: Generators are iterables, a kind of iterable you can only iterate over once.
    print('=' * 50)
    print('Generators do NOT store all the values in memory, they generate the values on the fly.')
    mygenerator = (x * x for x in range(5))
    print('type of mygenerator: ', type(mygenerator))
    for i in mygenerator:
        print(i)
    # you can NOT iterate the generator a second time since generator can only use once.
    # for i in mygenerator: ERROR

    # CLEARLY: 
    # `yield` is a keyword that like `return`, except the function will return a generator.
    print('=' * 50)
    def CreateGenerator(True_or_False):
        mylist = range(4)
        print('he i,   h  ei')
        if not True_or_False:
            print('false: not to yield.')
            #return 'ended ...'
            yield   # you can yield nothing
        for x in mylist:
            yield x * x * x
        print('ha o,   h  a_')

    True_or_False = True # False
    mygenerator = CreateGenerator(True_or_False)
    print('type of the created object: ', type(mygenerator))
    print('the object is: ', mygenerator)
    for i in mygenerator:
        print(i)

    # NOTE: to master `yield`, you must understand that when you call the function (e.f. CreateGenerator),
    # the code you have written in the function body does NOT run. 
    # The function only return a generator, which is a bit tricky.
    # NOTE: now the hard part: 
    #      the 1st time the `for` calls the generator created from you function, it will run the code in 
    #      your function from beginning UNTIL it hits `yield`, then it will return the 1st value of the loop.
    #      Then each other call will run the loop written in the function one more time, and return the next
    #      value until there's no value to return. 
    #NOTE: 3 parts: prior-mainbody (e.f. loop), mainbody or mainloop, post-mainbody
    #NOTE: ?? always need to use `for` to trigger the execution??

    # the generator is considered empty once the function run, but it does NOT hit `yield` anymore. 

    # control a generator exhaustion
    class BOC():
        crisis = False
        def create_atm(self):
            while self.crisis:
                yield "RMB 100"
                #print ('RMB 100')

    haidian_boc = BOC()
    corner_street_atm = haidian_boc.create_atm()
    #print(next(corner_street_atm))
    try:
        print(corner_street_atm.__next__())
    except:
        haidian_boc.crisis = True
        another_atm = haidian_boc.create_atm()
        #print(corner_street_atm.__next__())  # in corner_street_atm, crisis is still False
        print(another_atm.__next__())
        print(next(another_atm))
    
    # MORE about understanding keyword $yield: 
    #When you see a function with yield statements, apply this easy trick to understand what will happen:

    #   1, Insert a line result = [] at the start of the function.
    #   2, Replace each yield expr with result.append(expr).
    #   3, Insert a line return result at the bottom of the function.
    #   4, Yay - no more yield statements! Read and figure out code.
    #   5, Compare function to original definition.
    def yield123():
        yield 1
        yield 2
        yield 3
    iter_123 = yield123()
    print(next(iter_123))
    print(next(iter_123))
    print(next(iter_123))
    iter_123_ = yield123()
    print(next(iter_123_))
    print(iter(iter_123_))
    print(next(iter_123_))
    #print(next(iter_123_))
    print('bad usage: ')
    print(next(yield123()))  # only print 1
    print(next(yield123()))  # only print 1
    print(next(yield123()))  # only print 1

    # And, do NOT confuse your iterator 
