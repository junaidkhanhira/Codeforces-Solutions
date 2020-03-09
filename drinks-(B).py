n = int(input().strip())
l = list(int(x) for x in input().strip().split(' '))
s = 0

for i in range(n):
	s += l[i] / 100

r = (s / n) * 100

print(r)