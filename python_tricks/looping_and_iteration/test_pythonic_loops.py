## basic, show the evolution writing of 'for loop' from old c-style to pythonic style

if __name__ == '__main__':
    ef_items = ['ganghe', 'off', 'flavor', 'nuts']
    
    # c-style:
    print('old C-style for-loop: ')
    i = 0
    while i < len(ef_items):
        print(': ', ef_items[i])
        i += 1

    # 2nn c-style:
    print('2nd old C-style for-loop: ')
    for i in range(len(ef_items)):
        print(': ', ef_items[i])

    # a bit normal:
    print('1st pythonic way: ')
    for item in ef_items:
        print(': ', item)

    # classic pythonic:
    print('2nd enumerate: ')
    for i, item in enumerate(ef_items):
        print(f'{i}: {item}')

    # iterators in Python can return more than just one value. They can return tuples
    # with an arbitrary number of values that can then be unpacked right inside the for-statement.
    print('3rd, iterate items: ')
    linear_algebra = {
        'vec2d': 'x,y',
        'matrix': 'tensor',
        'basic': 'elements',
    }
    for item, content in linear_algebra.items():
        print(f'{item} -> {content}')

    #range() with start value, stop value and step size
    print('4th, stepped for loop: ')
    for i in range(0, 20, 4):
        print(f'stepped: {i}') 
