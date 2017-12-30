# My Solution
def calculate_years(principal, interest, tax, desired):
    #raise NotImplementedError("TODO: calculate_years")
    standard = principal
    years = 1
    if principal >= desired:
        return 0
    else:
        while principal < desired:
            i = interest*principal
            principal += i
            principal -= tax*i
            if principal >= desired:
                return years
            years += 1

# Cleaner:

def calculate_years2(principal, interest, tax, desired):
    years = 0
    
    while principal < desired:
        principal += (interest * principal) * (1 - tax)
        years += 1
        
    return years