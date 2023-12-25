p = [x.split(' ') for x in open('18.txt').read().strip().split('\n')]
dirs = {'R': (0, 1), 'U': (-1, 0), 'L': (0, -1), 'D': (1, 0)}

sign = lambda x: (x > 0) - (x < 0)
def solve(p):
    n = 0, 0
    E = []
    A = 0
    b = 0
    for (di, dj), r in p:
        b += r
        if dj:
            A += n[0] * r * dj
        n = n[0] + di * r, n[1] + dj * r
    A = abs(A)
    i = A - b // 2 + 1
    print(i + b)

solve([(dirs[d], int(r)) for d, r, c in p]) # p1
solve([(dirs['RDLU'[int(c[-2])]], int(c[2:-2], 16)) for d, r, c in p]) # p2
