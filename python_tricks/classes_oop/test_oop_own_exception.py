#

def hiphop(singer_name: str):
    print(singer_name)
    if len(singer_name) < 11:
        raise ValueError

# self-documenting
class DIYTooShortError(ValueError):
    pass

def validateTooShort(singer_name: str):
    print(singer_name)
    if len(singer_name) < 11:
        raise DIYTooShortError(singer_name)
    elif len(singer_name) > 20:
        raise ValueError

# create a custom exception hierarchy
class BaseExceptionError(ValueError):
    pass

class NameTooShortError(BaseExceptionError):
    pass

class NameTooLongError(BaseExceptionError):
    pass


if __name__ == '__main__':
    name = 'HotDog'
    #hiphop(name)
    validateTooShort(name)
