def nxRnd(k, nL):
	c = 0
	for i in nL:
		if i > 0 and nL[k-1] <= i:
			c += 1
	return c
 
 
n, k = map(int, input().split(" "))
nL = map(int, input().split(" "))
nL = list(nL)

print(nxRnd(k, nL))