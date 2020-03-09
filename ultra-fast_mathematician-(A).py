n1 = str(input().strip())
n2 = str(input().strip())

l = len(n1)
r = ''

for i in range(0, l):
	if n1[i] == n2[i]:
		r += '0'
	else:
		r += '1'

print(r)