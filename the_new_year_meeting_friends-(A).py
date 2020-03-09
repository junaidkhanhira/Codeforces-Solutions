l = list(int(x) for x in input().strip().split(' '))
l.sort()

d1 = l[2] - l[1]
d2 = l[1] - l[0]

print(d1 + d2)