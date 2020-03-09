n, m, a = map(int, input().strip().split())
 
i = n // a
if n % a != 0:
	i += 1
 
j = m // a
if m % a != 0:
	j += 1
 
print(i * j)