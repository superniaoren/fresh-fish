##

class NonRepr:
    def __init__(self, beatles, click15):
        self.band_britan = beatles
        self.band_native = click15

## add __str__ and __repr__ dunder methods
## BUT, inspecting the object in the console still gives you the object's id
## __str__ is one of python's 'dunder' (double-underscore) methods and 
## gets called when you try to convert an object into a string through the various
## means that are available
class WithStr:
    def __init__(self, beatles, click15):
        self.band_britan = beatles
        self.band_native = click15

    def __str__(self):
        return f'IQIYI: {self.band_native}, my favorite.'
    

if __name__ == '__main__':
    print("string conversion: every class needs a __repr__ : ")

    # only print class name and the id of the object instance 
    # (which is the object's memory address in CPython)
    nonrepr = NonRepr('jude', 'beidaihe')
    print(nonrepr)

    # with __str__
    withstr = WithStr('nov', 'penglei')
    print(withstr)
