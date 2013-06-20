import math
import itertools

def factors(n):
    """finds all the factors in number n and returns a list of all the factors"""
    sqrt = int(math.floor(math.sqrt(n)))
    print "number is", n
    # print "square root of the number is about", sqrt

    smaller_factors = set()
    all_factors = set()

    for i in xrange(1,sqrt+1):
        if n % i == 0:
            smaller_factors.add(i)

    for i in smaller_factors:
        all_factors.add(n/i)
    all_factors = all_factors.union(smaller_factors)
    print all_factors

    return all_factors

# for i in range(20):
#     factors(i)


def triangle_numbers():
    start = 1
    total = 0

    while True:
        total += start
        print "start", start, "total", total
        yield total
        start += 1

iterator = triangle_numbers()

for i in range(10):
    print iterator.next()

while True:
    number = iterator.next()
    factors(number)
    print "FACTORS OF THE NUMBER ARE", factors(number)
    if len(factors(number)) > 500:
        break

    # if number > 500:
    #     break
print "the winner is", number

# print factors(100)
# print len(factors(100))