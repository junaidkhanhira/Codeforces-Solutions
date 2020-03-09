s = input().strip()

sl = list()

for i in s:
	sl.append(i)

if len(set(sl)) % 2 == 0:
	print('CHAT WITH HER!')
else:
	print('IGNORE HIM!')
