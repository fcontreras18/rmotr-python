def nested_pyramid():
    pyramid = ''
    for i in range(1, 6):
        row = ''
        for j in range(i):
            row += '*'
        row += '\n'
        pyramid += row
    return pyramid


print(nested_pyramid())
