def square_digits(num):
    if num == 0: return 0
    else:
        arr = list(str(num))
        square = ""
        for i in arr: 
            square += str(int(i)**2)
        return int(square)
print(square_digits(9119))

# Shortened:

def square_digits2(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)