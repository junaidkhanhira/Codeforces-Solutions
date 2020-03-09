s = input().strip()

pi = (72, 81, 57)

for i in s:
	if ord(i) in pi:
		f = True
		print('YES')
		quit()
	else:
		f = False

if f == False:
	print('NO')