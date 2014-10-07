
# Special Pythagorean triplet
# Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


import math

# while a+b+c <= 1000:
# 	if a+b+c == 1000:
# 		print "we found a winner!!!", a, b, c
# 		break


def find_pythag_trips(n):
	""" finds n number of pythagorean triplets and returns a list with all of them"""
	list1 = []
	winner = ["JFOWIJFOEJFOEIJFOWEJFOEWIJFEOIFJOWEIFJOWEJFOEIWFJOIWEFJOEWFJOIWEFJOEWFJOIEWFJOEWIFJOIFOEWIJFOEWFJOEIWFJOEWJOEIF"]
	a = 3
	print "starting function 'find_pythag_trips'"
	while a<n:
#		print "starting first while loop"
		b = a + 1
		c = math.sqrt(a**2 + b**2)
		print a, b, c
		if c - int(c) == 0:
			print a, b, c, "is a triplet"
			list1.append([a,b,c])
		if a+b+c == 1000:
			winner.append([a,b,c])
		while b/a <20:
#			print "starting second while loop"
			b += 1
			c = math.sqrt(a**2 + b**2)
			print a, b, c
			if c - int(c) == 0:
				print a, b, c, "is a triplet"
				list1.append([a,b,c])
			if a+b+c == 1000:
				winner.append([a,b,c])
		a += 1
#		print "end of first while loop"
	return list1, winner


print find_pythag_trips(500)