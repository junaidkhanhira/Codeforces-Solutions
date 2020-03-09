n, k = map(int, input().strip().split(' '))
rt = 240 - k
st = 0
c = 0

for i in range(1, n + 1):
	st += (i * 5)
	if st > rt:
		break
	else:
		c += 1

print(c)