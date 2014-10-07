
# Largest palindrome product
# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(n):
	if str(n) == str(n)[::-1]:
		return True
	else:
		return False

palindromes = []

for i in xrange(1000):
	for j in xrange(1000):
		if is_palindrome(i*j):
			palindromes.append(i*j)

print(max(palindromes))