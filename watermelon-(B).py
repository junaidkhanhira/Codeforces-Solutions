n = int(input().strip())
n1 = 1
n2 = n - 1

fl = False

for i in range(0, n):
	if n1 == 0 or n2 == 0:
		break
	elif (n1 % 2 == 0) and (n2 % 2 == 0):
		fl = True
		break
	else:
		n1 += 1
		n2 -= 1

if fl:
	print('YES')
else:
	print('NO')