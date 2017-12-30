def countBits(n):
    if n == 0: return 0
    else:
        count = 0
        while n >= 1:
            print(n%2)
            if n % 2 == 1:
                count+=1
            n = n//2
    return (count)

# Optimal Solution
def countBits(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total
