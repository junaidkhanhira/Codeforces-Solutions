for i in range(0, 5):
	n = list(input().strip().replace(' ', ''))
	for ni in n:
		if int(ni) == 1:
			r = n.index(ni)+1
			c = i+1
			break
		
r = abs(r - 3) + abs(c - 3)

print(r)