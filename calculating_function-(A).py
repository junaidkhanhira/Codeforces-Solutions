n = int(input().strip())

if n % 2 == 0:
	t = n / 2
else:
	t = (n - 1) / 2
	t = t - n

print(int(t))