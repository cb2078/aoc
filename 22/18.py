p=open('18.txt').read().strip().split('\n')
p=[tuple(map(int,x.split(','))) for x in p]
b=lambda x, y: 1 == sum(abs(x[i]-y[i]) for i in range(3))
print(len(p) * 6 - sum(b(x, y) for x in p for y in p)) # 1
low, high = (f(x[i] + o for x in p for i in range(3)) for f, o in ((min, -1), (max, +1)))

q = [(low,) * 3]
v = set()
while q:
    *q, u = q
    if any(u[i] < low or u[i] > high for i in range(3)) or u in v or u in p:
        continue
    v |= {u}
    q += [u[:i] + (u[i] + o,) + u[i + 1:] for i in range(3) for o in (-1, 1)]
print(sum(b(x, y) for x in p for y in v)) # 2
