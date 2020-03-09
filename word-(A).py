s = input().strip()

uc = 0
lc = 0

for i in s:
	if i.islower():
		lc += 1
	else:
		uc += 1

if lc >= uc:
	s = s.lower()
else:
	s = s.upper()

print(s)