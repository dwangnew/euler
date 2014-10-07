# First problem from project euler. This isn't that bad for now!

# "Project Euler is a series of challenging mathematical/computer programming problems ... [which] the use of a computer and programming skills will be required to solve most problems."
# https://projecteuler.net

# problem 1 text: 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


n = 1000
total = 0

for i in range(n):
	if (i%3 == 0):
		print i, " is divisible by 3"
		total += i
	else:
		if (i%5 == 0):
			print i, " is divisible by 5"
			total += i

print "total = ", total
