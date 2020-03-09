n = int(input().strip())

c = 0

for i in range(0, n):
	p, q = map(int, input().strip().split(' '))
	if abs(q - p) >= 2:
		c += 1

print(c)