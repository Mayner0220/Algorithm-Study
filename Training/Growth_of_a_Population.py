# https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python

def nb_year(p0, percent, aug, p, count=0):
    if (p0 >= p):
        return count
    else:
        count += 1
        population = p0 + p0 * (percent/100) + aug

        return nb_year(population, percent, aug, p, count)

print(nb_year(1500, 5, 100, 5000))
print(nb_year(1500000, 2.5, 10000, 2000000))