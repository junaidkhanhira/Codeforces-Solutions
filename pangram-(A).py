n = int(input().strip())
s = input().strip().lower()

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
	'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if n >= 26:
	for i in range(0, 26):
		if a[i] in s:
			fl = True
		else:
			print('NO')
			quit()
	if fl == True:
		print('YES')
else:
	print('NO')