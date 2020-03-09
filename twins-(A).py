n = int(input().strip())
s = input().strip()
l = list(int(x) for x in s.split(' '))
l.sort(reverse = True)

t1 = 0
t2 = 0
c = 0

for i in l:
	t1 += i

for i in l:
	t2 += i
	t1 -= i
	c += 1
	if t2 > t1:
		break

print(c)