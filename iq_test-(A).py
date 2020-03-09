n = int(input().strip())
l = list(int(x) for x in input().strip().split(' '))
odd = True

if (l[0] % 2 == 0 and l[1] % 2 ==0) or (l[0] % 2 == 0 and l[2] % 2 == 0) or l[1] % 2 == 0 and l[2] % 2 == 0:
	odd = False

for i in range(n):
	if odd:
		if l[i] % 2 == 0:
			print(i + 1)
			break
	else:
		if l[i] % 2 != 0:
			print(i + 1)
			break