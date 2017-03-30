def advanced_nested_pyramid(start=1, last=5, char='*'):
    pyramid = ''
    for i in range(start, last+1):
        row = ''
        for j in range(i):
            row += char
        row += '\n'
        pyramid += row
    return pyramid


print(advanced_nested_pyramid())

"""
def advanced_nested_pyramid(start=1, last=5, char='*'):
    i = start
    pyramid = ''

    while i <= last:
        row = char * i
        pyramid += row
        pyramid += '\n'
        i += 1
    return pyramid
"""