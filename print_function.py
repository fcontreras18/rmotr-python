def print_function(final):
    start = '123'
    if final > 3:
        new_list = list(range(4, final + 1))
        for elem in new_list:
            start += str(elem)
        return start
    else:
        return start


print(print_function(10))
print(print_function(20))
print(print_function(3))

"""
Python 2:
from __future__ import print_function
print(*range(1, input() + 1), sep="") 

Python 3:
print(*range(1, int(input()) + 1), sep="")
"""