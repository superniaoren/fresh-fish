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
