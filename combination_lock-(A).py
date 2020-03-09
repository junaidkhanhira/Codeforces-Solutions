n = int(input().strip())
n1 = str(input().strip())
n2 = str(input().strip())
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
r = 0

for i in range(n):
	s1 = abs(int(n1[i]) - int(n2[i]))
	s2 = abs(int(n1[i]) - 0) + abs(int(n2[i]) - 9) + 1
	s3 = abs(int(n2[i]) - 0) + abs(int(n1[i]) - 9) + 1
	r += min(s1, s2, s3)

print(r)