def triple_nested_loop(num=5):
    output = ''
    for i in range(1, num + 1):
        for j in range(num - i):
            output += '.'
        for m in range(i):
            output += str(i)
        output += '\n'
    return output


print(triple_nested_loop())
print(triple_nested_loop(7))
