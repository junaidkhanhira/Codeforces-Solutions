n = int(input().strip())

def isComposite(n):
	fl = False
	for i in range(2, n):
		if n % i == 0:
			return True
			break
	return fl

for i in range(1, n):
	a = i
	b = n - 1
	if isComposite(a) and isComposite(b):
		print(a, b)
		break
	n -= 1