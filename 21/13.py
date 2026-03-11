with open('13.txt') as f:
    c, i = f.read()[:-1].split('\n\n')
    c = set(tuple(map(int, s.split(','))) for s in c.split('\n'))
    i = [s.split(' ')[-1].split('=') for s in i.split('\n')]
    i = [(d, int(l)) for d, l in i]

def f(c, l):
    return l * 2 - c if c > l else c

# 1
for d, l in i[:1]:
    c = {(f(x, l), y) if d == 'x' else (x, f(y, l))
         for x, y in c}
print(len(c))

# 2
for d, l in i[1:]:
    c = {(f(x, l), y) if d == 'x' else (x, f(y, l))
         for x, y in c}
w, h = (1 + max(p[i] for p in c) for i in (0, 1))
g = [[' ' for _ in range(w)] for _ in range(h)]
for x, y in c:
    g[y][x] = '#'
print('\n'.join(''.join(x) for x in g))
