s = input().strip()

l = list(int(x) for x in s.split('+'))
l.sort()

r = '+'.join(str(x) for x in l)

print(r)