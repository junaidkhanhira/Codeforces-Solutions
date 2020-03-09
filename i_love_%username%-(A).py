n = int(input().strip())
s = input().strip()
l = list(int(x) for x in s.split(' '))

mn = l[0]
mx = l[0]
c = 0

for i in range(1, n):
	if l[i] > mx:
		c += 1
		mx = l[i]
	elif l[i] < mn:
		c += 1
		mn = l[i]

print(c)