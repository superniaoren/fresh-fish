# test sets and multisets

if __name__ == '__main__':
    print('\n#1, ', '-' * 40)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    squares = {x * x for x in range(10)}
    empty = {}
    print('set vowels: ', vowels)
    print('set squares: ', squares)
    print('set empty: ', empty, ', type: ', type(empty), ', SO, not a set, but DICT')

    chars = set('masked')
    chars = chars.intersection(vowels)
    print('chars & vowels: ', chars)
    update = chars.add('Z')
    #update = chars.add({'Z'})
    if not update:
        print('seems set.add not work ???')
    else:
        print('chars add: ', update)
    update = chars.union('E', 'F')
    print('chars union" ', update)

    # frozenset - Immutable sets: no insert or deletion
    print('\n', '-' * 40)
    korea = frozenset({'k', 'o', 'r', 'e', 'a'})
    try:
        immutable = korea.add('n')
    except:
        print('frozenset are immutable.')

    # frozenset is hashable and can be used as dictionary keys:
    askey = { frozenset({1, 2, 3}): 'north'}
    print('frozenset as key: ', askey[frozenset({1,2,3})])
    
    # multisets: collections.Counter
    from collections import Counter
    
    # but why update not work ?
    delay_cn = Counter()
    inventory = Counter()
    loot = {'sword': 3, 'zeta': 10}
    boot = {'sword': 1, 'dprk': +1} # dprk: -1
    print('type of loot: ', type(loot))
    inventory = delay_cn.update(loot)
    print('Counter $inventory: ', inventory)
    print('Counter tmp $inventory: ', delay_cn.update(loot))
    print('Counter $delay_cn: ', delay_cn)
    print('length of delay_cn = ', len(delay_cn))
    print('sum of delay_cn = ', sum(delay_cn.values()))
    #if not inventory:
    #    print(inventory.update(boot))
