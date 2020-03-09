n = int(input().strip())
n += 1

for i in range(1, n):
	s = input().strip()
	if len(s) > 10:
		fs = s[0] + str(len(s) - 2) + s[-1]
	else:
		fs = s
	print(fs)