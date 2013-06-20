past1 = 2
past2 = 1
current = 0
total = 2
n = 100


for i in range(n):
	current = past1 + past2
	if (current > 4000000):
		break
	print "Fibbnacci number ", i+3, " is ", current
	past2 = past1
	past1 = current
	if (current%2 == 0):
		total += current

print "total of even numbered Fibonacci numbers is ", total