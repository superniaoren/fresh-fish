#

def hiphop(singer_name: str):
    print(singer_name)
    if len(singer_name) < 11:
        raise ValueError

if __name__ == '__main__':
    name = 'HotDog'
    hiphop(name)
