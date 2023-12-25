p = [s.split('\n') for s in open('19.txt').read().strip().split('\n\n')]

__A = lambda: sum(V)
__R = lambda: 0

for l in p[0]:
    n, b = l[:-1].split('{')
    b = b.split(',')
    C = [s.split(':') for s in b[:-1]]
    s =('__' + n + ' = lambda: ' +
        ' '.join(f'__{c[1]}() if {c[0]} else' for c in C) +
        ' __' + b[-1] + '()')
    # print(s)
    exec(s)

r = 0
for l in p[1]:
    s = l[1:-1].replace(',', ';')
    V = [int(''.join(filter(str.isdigit, s))) for s in l.split(',')]
    # print(s)
    exec(s)
    r += __in()

print(r) # p1

f = {}
for l in p[0]:
    n, b = l[:-1].split('{')
    b = b.split(',')
    C = []
    for s in b[:-1]:
        c, r = s.split(':')
        c = (c[0], c[1], int(c[2:]))
        C.append([c, r])
    f[n] = [*C, b[-1]]

def split(d, k, v):
    d0 = d.copy()
    d0[k] = (d[k][0], v)
    d1 = d.copy()
    d1[k] = (v, d[k][1])
    return d0, d1

import math
def solve(n, d):
    s = 0
    if n == 'R':
        return s
    if n == 'A':
        return math.prod(v[1] - v[0] for v in d.values())
    for (k, op, r), N in f[n][:-1]:
        if op == '<':
            D, d = split(d, k, r)
        else:
            d, D = split(d, k, r + 1)
        s += solve(N, D)
    s += solve(f[n][-1], d)
    return s

print(solve('in',{k: (1, 4001) for k in 'xmas'})) # p2
