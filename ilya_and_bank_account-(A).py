n = int(input().strip())

if n < 0:
	s = str(n)
	n1 = int(s[:-2] + s[-1])
	n2 = int(s[:-1])
	if n1 > n2:
		print(n1)
	else:
		print(n2)
else:
	print(n)
