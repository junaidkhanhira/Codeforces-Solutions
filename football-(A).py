s = input().strip()
 
ln = 1
fln = 1
cv = ''
 
for i in s:
	if i == cv:
		ln += 1
		if ln > fln:
			fln = ln
	else:
		ln = 1
	cv = i
	
if fln >= 7:
	print('YES')
else:
	print('NO')
