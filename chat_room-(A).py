s = input().strip()
h = ['h', 'e', 'l', 'l', 'o']

p = 0
l = len(h)

for i in s:
	if i == h[p]:
		p += 1
	if p >= l:
		break

if p == l:
	print('YES')
else:
	print('NO')