f = '21.txt'; p = open(f).read().strip().split('\n')
w, h = len(p[0]), len(p)
assert w == h

for i in range(w):
    for j in range(w):
        if p[i][j] == 'S':
            S = i, j

from collections import deque
def solve(N):
    q = deque([(*S, 0)])
    v = set()
    c = 0
    while q:
        i, j, n = q.popleft()
        if n > N:
            continue
        if (i, j) in v:
            continue
        else:
            v.add((i, j))
        c += n % 2 == N % 2
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if p[(i + di) % w][(j + dj) % w] == '#':
                continue
            q.append((i + di, j + dj, n + 1))
    return c

print(solve(64)) # p1

N = 26501365
k = (N - S[0]) // w
x = (N + S[0]) % w
y = [solve(x // 2 + i * w) for i in range(3)]
a = (y[2] - 2 * y[1] + y[0]) // 2
b = y[1] - y[0] - a
c = y[0]
f = lambda x: a * x ** 2 + b * x + c
print(f(k)) # p2
