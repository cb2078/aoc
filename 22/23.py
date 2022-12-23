from collections import defaultdict
from itertools import product, count

p=open('23.txt').read().strip().split('\n')
g=[(i, j) for i in range(len(p)) for j in range(len(p[0])) if p[i][j] == '#']

def bounds(g):
    return tuple(f(x[i] for x in g) for i in range(2) for f in (min, max))

def pp(g):
    imin, imax, jmin, jmax = bounds(g)
    return '\n'.join(''.join('.#'[(i, j) in g] for j in range(jmin, 1 + jmax)) for i in range(imin, 1 + imax)) + '\n'

dirs = [[(-1,  0), (-1,  1), (-1, -1)],
        [( 1,  0), ( 1,  1), ( 1, -1)],
        [( 0, -1), ( 1, -1), (-1, -1)],
        [( 0,  1), ( 1,  1), (-1,  1)]]

# print(pp(g))
for n in count():
    gg = defaultdict(list)
    no_move = True
    for i, j in g:
        if all((i + di, j + dj) not in g for di, dj in product([-1, 0, 1], repeat = 2) if (di, dj) != (0, 0)):
            gg[i, j] += [(i, j)]
            continue
        no_move = False
        for d in [(i + n) % 4 for i in range(4)]:
            if all((i + di, j + dj) not in g for di, dj in dirs[d]):
                gg[i + dirs[d][0][0], j + dirs[d][0][1]] += [(i, j)]
                break
        else:
            gg[i, j] += [(i, j)]
    assert(len([x for y in gg.values() for x in y]) == len(g))
    g = sum((gg[i, j] if len(gg[i, j]) > 1 else [(i, j)] for i, j in gg), start = [])
    print('== End of round', 1 + n, '==')
    # print(pp(g))
    if n + 1 == 10:
        imin, imax, jmin, jmax = bounds(g)
        print((imax - imin + 1) * (jmax - jmin + 1) - len(g)) # 1
    elif no_move:
        print(n + 1) # 2
        break
