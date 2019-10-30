## 
## Python yield is confusing. It's always tied to Python genertor
## https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

if __name__ == '__main__':
    print('review and learn yield again: ')
    print('to understand what `yield` is, U should first understand what `generator` is. ') 
    # for example, create an iterable var:
    mylist = [x * x for x in range(5)]
    print('type of mylist: ', type(mylist))
    for i in mylist:
        print(i)
    # here  mylist is an iterable. everything you can use 'for ... in ...' on is an iterable.
    # these iterables are handy cause you can read them as much as you wish,
    # BUT you store all the values in memory and this is not always you want when you have 
    # a lot of values.

    # generators: Generators are iterables, a kind of iterable you can only iterate over once.
    print('Generators do NOT store all the values in memory, they generate the values on the fly.')
    mygenerator = (x * x for x in range(5))
    print('type of mygenerator: ', type(mygenerator))
    for i in mygenerator:
        print(i)
    # you can NOT iterate the generator a second time since generator can only use once.
    # for i in mygenerator: ERROR

    # CLEARLY: 
    # `yield` is a keyword that like `return`, except the function will return a generator.
    def CreateGenerator():
        mylist = range(4)
        print('he i,   h  ei')
        for x in mylist:
            yield x * x * x
        print('ha o,   h  a_')

    mygenerator = CreateGenerator()
    print('type of the created object: ', type(mygenerator))
    print('the object is: ', mygenerator)
    for i in mygenerator:
        print(i)

    # NOTE: to master `yield`, you must understand that when you call the function (e.f. CreateGenerator),
    # the code you have written in the function body does NOT run. 
    # The function only return a generator, which is a bit tricky.
    # NOTE: now the hard part: 
    #      the 1st time the `for` calls the generator created from you function, it will run the code in 
    #      your function 




