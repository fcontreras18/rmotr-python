def banana_dict(num):
    count = 1
    banana = 'banana'
    a_dict = {}
    while count <= num:
        b = (banana * count)
        a_dict[b] = count
        count += 1
    return a_dict


banana_dict(4)
