n = str(input().strip())

c = 0

for i in n:
	if i == '7' or i == '4':
		fl = True
		c += 1
	else:
		fl = False

if c == 7 or c == 4:
	print('YES')
elif fl == True and (c == 7 or c == 4):
	print('YES')
else:
	print('NO')