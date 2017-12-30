# MY solution
def unique_in_order(iterable):
    pass
    if len(iterable) <=0:
        return []
    else:
        l = list(iterable)
        unique = []
        unique.append(l[0])
        for val in l:
            if ord( str(unique[len(unique)-1]) ) != ord(str(val)):
                unique.append(val)
        return unique

print( unique_in_order('') )

# Optimal Solution
def unique_in_order1(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result
