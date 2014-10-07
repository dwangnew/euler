#### I believe the first version was a mess so I redid it

# Largest prime factor
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

n = 600851475143
sqrt = math.sqrt(n)

print "number is", n
print "square root of the number is", sqrt

int_sqrt = int(math.floor(sqrt))
print int_sqrt

def factors(number):
	factors = []
	for i in xrange(number):
		if i != 0:
			if 600851475143%i == 0:
				factors.append(i)
	return factors

factors = factors(int_sqrt)
print factors

larger_factors = []
for i in factors:
	larger_factors.append(600851475143/i)

print larger_factors


def is_prime(number):
	counter = 0
	for i in xrange(number):
		if (i != 0) and (i != 1):
			if number%i != 0:
				counter += 1
			else:
				break
	if counter == number - 2:
		return True
	else:
		return False

for i in factors:
	print is_prime(i)

for i in larger_factors:
	print is_prime(i)
