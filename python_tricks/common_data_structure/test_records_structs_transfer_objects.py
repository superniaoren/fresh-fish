# record, provide named fields 
# 

if __name__ == '__main__':
    ## dict, also called maps or associative arrays 
    ## there's little protection against misspelled field names.
    ## these properties can introduce surprising bugs.
    ## be a trade-off to be made between convenience and error resilience.
    print('\n', '-' * 40, " simple dict ")
    gods = {
        'cui': 'marriage',
        'cox': True,
        'grade': -1,
    }
    print('simple data object: [dict]: ', gods)

    
    print('\n', '-' * 40, " immutable tuple ")
    print('\n\n tuple cost less memory than list: ')
    import dis
    print('\n\n constructing a tuple constant SHOULD take a single LOAD_CONST opcode:')
    dis.dis(compile("('mood', 2.1414, True, False)", '', 'eval'))
    dis.dis(compile("('mood', 2.1414, 'true', 'false')", '', 'eval'))
    print('\n\n constructing a list object SHOULD take several LOAD_CONST opcode:')
    dis.dis(compile("['mood', 2.1414, True, False]", '', 'eval'))
    dis.dis(compile("['mood', 2.1414, 'true', 'false']", '', 'eval'))

    print('a downside: tuple can only be pulled out by accessing it through integer indexes:')
    print('thus user may mixing up the filed order .')
    plain_tpls = ('mood', 2.1414, True, False)
    print('[1]:', plain_tpls[1])


    print('\n', '-' * 40, " custom class ")
    print('more work, more control. use regular python classes as record data types.')
    print('the default string representation for objects instantiated from custom classes is not helpful.')
    print('To fix that, you may have to add your own __repr__ method.')
    class DIY:
        def __init__(self, color, weight, skin):
            self.color = color
            self.weight = weight
            self.skin = skin

        def __repr__(self):
            return (f'color({self.color!r}),'
                   f'weight({self.weight!a}),'
                   f'skin({self.skin}),')

    diy1 = DIY('purple', 291., 'Black')
    diy2 = DIY('orange', -12., 'Brown')
    print(diy1)
    print(diy2)
    # classes are mutable, if wanna add more access control and to create read-only fields using @property decorator
    diy1.color = 'grey'
    diy2.skin = 'unknown'
    print(diy1)
    print(diy2)



    print('\n', '-' * 40, " struct.Struct, serialized C structs")
    from struct import Struct
    xstruct = Struct('i?f')
    xdata = xstruct.pack(1999999, 'ssd', -3.145339)
    print('xdata(serialized): ', xdata)
    ydata = xstruct.unpack(xdata)
    print("ydata(unpacked): ", ydata)
    print('type of unpacked ydata: ', type(ydata))
    print(ydata[1])
    
    

    print('\n', '-' * 40, " types.SimpleNamespace, Fancy, Attribute Access")
    from types import SimpleNamespace
    xsimple = SimpleNamespace(band='new pants',
                              vocal="peng lei",
                              bass='zhao meng',
                              keyboarder='pang kuan',
                              drummer='hayato',
                              best_elbum='tiger & dragon')
    print('SimpleNamespace has default repr: ', xsimple)
    xsimple.band='new pants forever'
    del xsimple.best_elbum
    print('SimpleNamespace is mutable: ', xsimple)



    print('\n', '-' * 40, " collections.namedtuple, Convenient Data Objects")
    from collections import namedtuple
    from sys import getsizeof
    xNamed = namedtuple('Class_Name', 'drummer vocla bass keyboards')
    print('type: ', type(xNamed))
    xband = xNamed('hayato', 'peng lei', 'zhao meng', 'pang kuan')
    print('type: ', type(xband))
    print('xband namedtuple: ', xband)
    print('xband.bass= ', xband.bass)



    print('\n', '-' * 40, " typing.NamedTuple, Improved Namedtuples")
    from typing import NamedTuple
    class xNT(NamedTuple):
        band: str
        drummer: str
        vocal: str
        bass: str

    hdge = xNT('hedgehog', 'shi lu', 'zi jian', 'yi fan')
    print(hdge)
    # just type hint, no forced check
    hdge = xNT('hedgehog', 99999, 'zi jian', 'yi fan')
    print(hdge)

