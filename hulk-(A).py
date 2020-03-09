n = int(input().strip())

s = ''

for i in range(1, n+1):
	s1 = 'that I hate'
	s2 = 'that I love'
	if i == 1:
		s += 'I hate'
	elif i > 1 and i % 2 != 0:
		s += ' that I hate'
	else:
		s += ' that I love'

s += ' it'

print(s)