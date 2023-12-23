p = list(map(list, open('14.txt').read().strip().split('\n')))
w, h = len(p[0]), len(p)
assert w == h

# for l in p:
#     print(''.join(l))

def tilt(p):
    for j in range(w):
        moving = True
        while moving:
            moving = False
            for i in range(w - 1):
                    if p[i + 1][j] == 'O' and p[i][j] == '.':
                        moving = True
                        p[i][j], p[i + 1][j] = p[i + 1][j], p[i][j]

weight = lambda p: sum((w - i) * (p[i][j] == 'O') for i in range(w) for j in range(w))

from copy import deepcopy
p_ = deepcopy(p)
tilt(p_)
print(weight(p_)) # p1

rot = lambda m: list(map(list, zip(*m[::-1])))

def cycle(p):
    for _ in range(4):
        tilt(p)
        rp = rot(p)
        for i in range(w):
            p[i] = rp[i]

n = 1000000000
ps = []
ls = []
while True:
    cycle(p)
    x = weight(p)
    if str(p) in ps:
        i = ps.index(str(p))
        l = len(ps)
        print(ls[i + (n - i) % (l - i)]) # p2
        break
    else:
        ps.append(str(p))
        ls.append(x)
