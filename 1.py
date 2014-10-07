# First problem from project euler
# This isn't too hard!
# https://projecteuler.net

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
