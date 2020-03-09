import sys

n = int(input().strip())
c = 0
r = 0

if n % 5 == 0:
	c = int(n / 5)
	print(c)
	sys.exit()
else:
	c = int(n // 5)
	r = n % 5
	n = r

if n % 4 == 0:
	c += int(n / 4)
	print(c)
	sys.exit()
else:
	c += int(n // 4)
	r = n % 4
	n = r

if n % 3 == 0:
	c += int(n / 3)
	print(c)
	sys.exit()
else:
	c += int(n // 3)
	r = n % 3
	n = r

if n % 2 == 0:
	c += int(n / 2)
	print(c)
	sys.exit()
else:
	c += int(n // 2)
	r = n % 2

print(c + r)