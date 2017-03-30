def variable_size_box(num, char):
    box = ''
    for i in range(num):
        row = ''
        for j in range(num):
            row += char
        row += '\n'
        box += row
    return box


print(variable_size_box(4, 'x'))
