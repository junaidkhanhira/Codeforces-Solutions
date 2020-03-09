s = input().strip()

if len(s) == 1:
	if s.islower():
		print(s.upper())
		quit()
	else:
		print(s.lower())
		quit()

if s.islower():
	print(s)
	quit()
elif s.isupper():
	print(s.lower())
	quit()
else:
	sl = list()
	c = 0
	for i in s:
		if c == 0:
			if i.islower():
				sl.append(i.upper())
			else:
				sl.append(i)
		else:
			if i.isupper():
				sl.append(i.lower())
			else:
				print(s)
				quit()
		
		c += 1

	fs = ''.join(sl)

	print(fs)
