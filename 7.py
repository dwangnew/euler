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

def list_primes(n):
	'''checks each number up to n and prints it out if it is prime'''
	counter = 1
	for i in xrange(n+1):
		if is_prime(i):
			counter += 1
			print i, "is prime", "#", counter

def find_prime(n):
	'''finds the nth prime number'''
	i = 1
	current_number = 2
	while i<n :
		current_number += 1
		if is_prime(current_number):
			i += 1
	print "the #", i, "prime number is", current_number
	return current_number

list_primes(100)
find_prime(25)
find_prime(10001)