f = open('14.txt').read()[:-1].split('\n\n')
p = P = f[0]
r = dict(s.split(' -> ') for s in f[1].split('\n'))

# 1
for _ in range(10):
    p = ''.join(c + r[c + p[i + 1]]
                for i, c in enumerate(p[:-1])) + p[-1]
f = [p.count(c) for c in r.values()]
print(max(f) - min(f))

# 2
p = P
d = {k: 0 for k in r}
for i in range(len(p) - 1):
    d[p[i: i + 2]] += 1
m = {k: (k[0] + v, v + k[1]) for k, v in r.items()}

for _ in range(40):
    D = {k: 0 for k in r}
    for k in d:
        D[m[k][0]] += d[k]
        D[m[k][1]] += d[k]
    d = D
f = {c: 0 for c in r.values()}
for k, v in d.items():
    f[k[0]] += v
    f[k[1]] += v
f[p[0]] += 1
f[p[-1]] += 1
f=f.values()
print((max(f) - min(f)) // 2)
