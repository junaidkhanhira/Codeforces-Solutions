v = ('a', 'o', 'y', 'e', 'u', 'i')
s = input().strip()
s = s.lower()
sl = list(s)
r = list()
 
for i in sl:
	if i in v:
		r.append('')
	else:
		r.append('.' + i)
 
r = ''.join(r)

print(r)