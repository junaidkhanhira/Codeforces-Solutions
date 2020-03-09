import sys

n, t = map(int, input().strip().split(' '))

r = '1'

r += '0' * (n - 1)
nx = r + '0'
r = int(r)
nx = int(nx)

for i in range(r, nx):
	if t != 0:
		if i % t == 0:
			print(i)
			sys.exit()

print(-1)
