s = input().strip()
t = input().strip()

sl = len(s)
tl = len(t)
nt = ''

if sl == tl:
	for i in range(tl-1, -1, -1):
		nt += t[i]
	if s == nt:
		print('YES')
	else:
		print('NO')
else:
	print('NO')