def remove_Es(a_string):
    a_list = list(a_string)
    a_list.remove('E')
    a_list.remove('e')
    a_list = ''.join(a_list)
    return a_list


print(remove_Es('Erice'))
