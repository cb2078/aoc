p = open('22.txt').read().strip().split('\n')
p = [[list(map(int, x.split(','))) for x in l.split('~')] for l in p]
p.sort(key = lambda b: b[0][2])
l = len(p)
assert all(p[i][0] <= p[i][1] for i in range(l))

def axis(i):
    for a in range(3):
        if p[i][0][a] != p[i][1][a]:
            return a
    return 0

def below(i, xy):
    for j in range(i)[::-1]:
        if all(p[j][0][k] <= xy[k] <= p[j][1][k]
               for k in range(2)):
            return j

from collections import defaultdict
b = defaultdict(list)
for i in range(l):
    a = axis(i)
    for r in range(p[i][1][a] + 1 -  p[i][0][a]):
        xy = [p[i][0][k] + (r if k == a else 0) for k in range(2)]
        b[i].append(below(i, xy))

def collides(i):
    a = axis(i)
    res = []
    for r in range(p[i][1][a] + 1 -  p[i][0][a]):
        j = b[i][r]
        if j is not None and p[i][0][2] <= p[j][1][2]:
           res.append(j)
    return res

parents = defaultdict(set)
children = defaultdict(set)
for i in range(l):
    p[i][0][2] -= 1
    p[i][1][2] -= 1
    js = []
    while p[i][0][2] > 0 and not (js := collides(i)):
        p[i][0][2] -= 1
        p[i][1][2] -= 1
    for j in js:
        parents[i].add(j)
        children[j].add(i)
    p[i][0][2] += 1
    p[i][1][2] += 1

print(sum(all(any(j in children[k] for k in range(l) if k != i)
              for j in children[i])
          for i in range(l))) # p1

from collections import deque
def bfs(i):
    q = deque([i])
    v = set()
    c = 0
    while q:
        i = q.pop()
        v.add(i)
        for j in children[i]:
            if not parents[j] - v:
                c += 1
                q.append(j)
    return c
print(sum(bfs(i) for i in range(l))) # p2
