n, k = map(int, input().strip().split())
a = input().strip().split(' ')
pk = k - 0.5
fl = True
s = 0
c = 0

for i in a:
	s += int(i)
sa = s / len(a)

while fl:
	if sa < pk:
		c += 1
		a.append(k)
		s += k
		sa = s / len(a)
	else:
		fl = False

print(c)
	