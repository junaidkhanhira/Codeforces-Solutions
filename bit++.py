n = int(input().strip())
n += 1
v = 0
 
for i in range(1, n):
	s = input().strip()
	if s == 'X++' or s == '++X':
		v += 1
	elif s == 'X--' or s == '--X':
		v -= 1
 
print(v)