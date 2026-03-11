with open('12.txt') as f:
    p = [s.split('-') for s in f.read()[:-1].split("\n")]
    g = {}
    
    def add(x):
        if x[0] not in g:
            g[x[0]] = [x[1]]
        else:
            g[x[0]].append(x[1])
    
    for P in p:
        add(P)
        add(P[::-1])

s = [['start', c] for c in g['start']]
res = 0
while s:
    S = []
    for p in s:
        if p[-1] == 'end':
            res += 1
            continue
            # print(p)
        for c in g[p[-1]]:
            if c.islower() and c in p:
                if c == 'start' or \
                        any(p.count(c) == 2 for c in p if c.islower()):
                    continue
            S.append(p + [c])
    s = S

print(res)
