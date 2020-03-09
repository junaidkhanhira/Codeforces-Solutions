k, n, w = map(int, input().strip().split(' '))

ks = 0

for i in range(1, w+1):
	ks += k*i

if ks > n:
	r = ks - n
	print(r)
else:
	print(0)