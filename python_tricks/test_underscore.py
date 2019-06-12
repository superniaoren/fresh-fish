import os

# global var:
_TestBase__bar = -1
_MangledGlobal__mangled = -1

class TestBase:
    def __init__(self):
        self.bar = 11
        self._bar = 22
        self.__bar = 33
    
    def print(self):
        print('bar = {}'.format(self.bar))
        print('_bar = {}'.format(self._bar))
        print('__bar = {}'.format(self.__bar))

    def _method(self):
        print('1, _method call')

    def __method(self):
        print('2, __method call')

# starts dunder vars would be named-mangling by Python interpreter
# but variables surrounded by a dunder prefix and postfix are left unscathed.
class MangledGlobal:
    def __init__(self):
        #self.__mangled = 99
        pass
    def mangle(self):
        return __mangled
        #return self.__mangled  # different

class PrefixPostfixTest:
    def __init__(self):
        self.__rand_var__ = 44


if __name__ == '__main__':
    tb = TestBase()
    print(dir(tb))
    tb.print()
    _TestBase__bar = 33333
    # here, it seems not the privilleges forbidden, but name-mangling forbidden
    print(tb.bar)
    print(tb._bar)
    print(tb._TestBase__bar)

    mg = MangledGlobal()
    print(mg.mangle())
    print(dir(mg))

    ppt = PrefixPostfixTest()
    print(ppt.__rand_var__)
    print(dir(ppt))

    for i in range(2):
        print('lolo')
        for j in range(4):
            print('hoho', j)
    # NOTE: still be valid: j
    print(j)
