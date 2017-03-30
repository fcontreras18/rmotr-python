def longest_key(a_dict):
    longest = ''
    if a_dict == {}:
        return None
    for key in a_dict:
        if len(key) > len(longest):
            longest = key
    return longest


print(longest_key({'hello': 'World', 'abc': 123}))
print(longest_key({'hello': 'World', 'abc': 123, 'eeeeeeee': 2}))
print(longest_key({}))
