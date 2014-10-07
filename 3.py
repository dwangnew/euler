
# Largest prime factor
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

number = 600851475143
# all_numbers = xrange(number)
# odd_numbers = [ x for x in xrange(number) if x%2 != 0 ]

# print all_numbers
# print odd_numbers

def list_primes(number):
	primes = []
	for i in xrange(number):
		if is_prime(i):
			primes.append(i)
	return primes

def is_prime(number):
	counter = 0
	for i in xrange(number):
		if (i != 0) and (i != 1):
			if number%i != 0:
				counter += 1
	if counter == number - 2:
		return True
	else:
		return False

def prime_factors(number):
	factors = []
	for i in list_primes(number):
		if number%i == 0:
			factors.append(i)
	return factors

def factors(number):
	factors = []
	for i in xrange(number):
		if i != 0:
			if number%i == 0:
				factors.append(i)
	return factors

# print(prime_factors(13195))
print(factors(13195))