import math

def is_prime(number):
	'''checks if a number is prime and returns True if it is prime, False if it is not'''
	if number%2 == 0:
		return False
	if number == 1:
		return False
#	print "checking if the number", number, "is prime"
	sqrt = int(math.floor(math.sqrt(number)))
#	print "the square root of the number is about", sqrt
	for i in xrange(2, sqrt+1):
		if number%i == 0:
			return False
	return True

def sum_primes(n):
	'''sums all primes up to n'''
	total = 2
	for i in xrange(n+1):
		if is_prime(i):
			total += i
			print i, "is prime"
			print "sum is now", total

sum_primes(2000000)