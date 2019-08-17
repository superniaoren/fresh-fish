## abc 

class Base:
    def vanish(self):
        raise NotImplementedError()
    
    def puff(self):
        raise NotImplementedError()

class Concrete(Base):
    def vanish(self):
        return 'vanish() called: what? could be considered a little rude...'

from abc import ABCMeta, abstractmethod
class ABCBase(metaclass=ABCMeta):
    @abstractmethod
    def vanish(self):
        pass

    @abstractmethod
    def puff(self):
        pass

class ABCConcrete(ABCBase):
    def puff(self):
        pass

if __name__ == "__main__":
    c = Concrete()
    print(c.vanish())

    try:
        print(c.puff())
    except NotImplementedError:
        print("the drawbacks: \n" \
              " 1st, instantiate Base just fine with getting an error. \n"
              " 2nd, provide incomplete subclasses- instantiating Concrete will \n"
              "      not raise an error until the missing method is called\n"
        )
    
    # subclass of ABCBase raise a TypeError at INSTANTIATION time whenever we forget 
    # to implement any abstract methods.
    assert issubclass(ABCConcrete, ABCBase)

    abc_c = ABCConcrete()
