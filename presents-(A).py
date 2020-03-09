n = int(input().strip())
p = input().strip().split(' ')

pl = list()

for i in p:
	if i != ' ':
		pl.append(int(i))

pl.insert(0, '')

fl = list()

for i in range(1, n+1):
	if i in pl:
		fl.append(str(pl.index(i)))

print(', '.join(fl).replace(', ', ' '))