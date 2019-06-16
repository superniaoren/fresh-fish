
name_uid = {
    561: 'VBL',
    19.0: 'Baozi',
    512: 'Godbel',
    373: 'PB',
}

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


if __name__ == '__main__':
    print(greeting(19.0))
    print(greeting(41))
