x = input().strip()
y = input().strip()
z = ''
n = len(x)
fl = True

for i in range(n):
	if x[i] < y[i]:
		fl = False
		break
	elif x[i] > y[i]:
		z += chr(ord(y[i]))
	elif x[i] == y[i] and ord(x[i]) < 122:
		z += chr(ord(x[i]) + 1)
	elif x[i] == y[i] and ord(x[i]) == 122:
		z += chr(ord(x[i]))
	else:
		fl = False
		break
		
if fl and len(z) > 0:
	print(z)
else:
	print(-1)