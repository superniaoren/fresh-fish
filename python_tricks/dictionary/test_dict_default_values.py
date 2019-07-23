
name_uid = {
    561: 'VBL',
    19.0: 'Baozi',
    512: 'Godbel',
    373: 'PB',
}

# dict query
def greeting(uid):
    # v0
    #return 'Alexander Yogoivanivch %s!' % name_uid[uid]
    # v1
    #if uid in name_uid:
    #    return 'Alexander Yogoivanivch: %s!' % name_uid[uid]
    #else:
    #    return 'Hi, there, and who\'re U: {}'.format(uid)
    # v2, EAFP, easier to ask for forgiveness than permission
    #try:
    #    return 'Alexander Yogoivanivch: %s!' % name_uid[uid]
    #except KeyError:
    #    return 'Hi, there, and who\'re U: {}'.format(uid)
    # v3, dict's get() method:
    return 'Alexander Yogoivanivch %s!' % name_uid.get(uid, 'Hi, there, and who\'re U:{}'.format(uid))

def customize_sort(input_dict):
    print('type of input: {}'.format(type(input_dict)))
    print('type of input.items: {}'.format(type(input_dict.items())))
    #default sort, with default keys
    default = sorted(input_dict.items())
    print(default)
    print('type of output: {}'.format(type(default)))

    # sort on values (not keys)
    #vsort = sorted(input_dict.items(), key=lambda x: x[0]) 
    vsort = sorted(input_dict.items(), key=lambda x: x[1]) 
    print(vsort)
    print('type of output: {}'.format(type(vsort)))

    # use operator module to replace the lambda-based index lookup
    import operator
    osort = sorted(input_dict.items(), key=operator.itemgetter(1))
    print(osort)
    print('type of output: {}'.format(type(osort)))

    # abs sort, NOTE: reverse = False by default
    asort = sorted(input_dict.items(), key=lambda x: abs(x[1]), reverse=True)
    print(asort)
    print('type of output: {}'.format(type(asort)))

if __name__ == '__main__':
    print(greeting(19.0))
    print(greeting(41))

    idict = {'a': 92, 'xs': 3, 'zoo':-4, 'yolo': 13}
    customize_sort(idict)
