def divisors(integer):
    divisors = []
    for i in range(1,integer+1):
        if integer % i == 0:
            divisors.append(i)
    if len(divisors) == 2 and divisors[0] == 1 and divisors[1] == integer:
        return (str(integer)+ " is prime")
    else:
        return divisors[1:len(divisors)-1]

print(divisors(4))

# Another Soltn

def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l