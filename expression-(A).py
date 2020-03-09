a = int(input().strip())
b = int(input().strip())
c = int(input().strip())

t = []

t.append(a + b + c)
t.append(a * b + c)
t.append(a + b * c)
t.append(a * b * c)
t.append(a * (b + c))
t.append((a + b) * c)

print(max(t))