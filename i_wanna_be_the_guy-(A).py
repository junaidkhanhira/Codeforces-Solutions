n = int(input().strip())
s1 = input().strip()
s2 = input().strip()
l1 = list((int(x) for x in s1.split(' ')))
l2 = list((int(x) for x in s2.split(' ')))
l1 = l1[1:]
l2 = l2[1:]
l = l1 + l2
fl = True

for i in range(1, n +1):
	if i not in l:
		fl = False
		break

if fl:
	print('I become the guy.')
else:
	print('Oh, my keyboard!')
