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