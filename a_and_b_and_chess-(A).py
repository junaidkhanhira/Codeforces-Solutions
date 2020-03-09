w = ''
b = ''
s = ''

for i in range(8):
	s += input().strip()

for i in s:
	if i != '.':
		if i.isupper():
			w += i
		else:
			b += i

def weight(s):
	d = {'q':9, 'r':5, 'b':3, 'n':3, 'p':1, 'k':0}
	c = 0
		
	for i in s:
		c += d[i.lower()]
		
	return c

if weight(w) > weight(b):
	print('White')
elif weight(b) > weight(w):
	print('Black')
else:
	print('Draw')