s1 = input().strip().lower()
s2 = input().strip().lower()
 
s1 = list(s1)
s2 = list(s2)
 
def wVal(s1, s2):
	for i, j in zip(s1, s2):
		if i > j:
			return 1
		elif i < j:
			return -1
		else:
			continue
	return 0
 
print(wVal(s1, s2))