s1 = input().strip()
s2 = input().strip()
s = input().strip()
l = list()
r = ''

for i in range(26):
	l.append([s1[i], s2[i]])

for i in s:
	if i.isnumeric():
		r += i
	else:
		if i.isupper():
			for x in l:
				if x[0] == i.lower():
					r += x[1].upper()
		else:
			for x in l:
				if x[0] == i:
					r += x[1]

print(r)