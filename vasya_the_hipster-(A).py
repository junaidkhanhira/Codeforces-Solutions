n1, n2 = map(int, input().strip().split(' '))

if n1 != n2:
	mx = max(n1, n2)
	mn = min(n1, n2)
	dc = mn
	rem = mx - mn
	if rem > 1:
		sc = int(rem / 2)
	else:
		sc = 0
else:
	dc = n1
	sc = 0

print(dc, sc)