a, b, c = map(int, input().split(' '))

if a == b:
	print('YES')
elif a != b and c == 0:
	print('NO')
else:
	if (b - a) % c == 0 and ((b - a) / c) > 0:
		print('YES')
	else:
		print('NO')