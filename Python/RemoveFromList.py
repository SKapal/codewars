def filter_list(l):
    filtered = []
    for i in l:
        if type(i) is not str:
            filtered.append(i)
    return filtered

# filter_list([1,2,'a','s'])
print( filter_list([1,2,'a','s']) ) 