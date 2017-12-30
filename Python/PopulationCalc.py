def nb_year(p0, percent, aug, p):
    # your code
    if p0 == p: return 0
    else:
        fracPercent = percent/100
        years = 0
        while p0<p:
            years += 1
            p0 += p0*fracPercent + aug
            if p0 >= p:
                return years


# Optimal solution:
def nb_year2(population, percent, aug, target):
    year = 0
    while population < target:
        population += population * percent / 100. + aug
        year += 1
    return year