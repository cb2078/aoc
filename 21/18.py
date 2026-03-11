from functools import reduce
from copy import deepcopy

def ld(s):
    d = -1
    a = []
    for c in s:
        if c == '[':
            d += 1
        elif c == ']':
            d -= 1
        elif c.isdigit():
            a.append([d, int(c)])
    return a

def red(a):
    for i, (d, v) in enumerate(a):
        if d >= 4:
            if i > 0:
                a[i - 1][1] += v
            if i + 2 < len(a):
                a[i + 2][1] += a[i + 1][1]
            a[i: i + 2] = [[d - 1, 0]]
            return red(a)
    for i, (d, v) in enumerate(a):
        if v >= 10:
            a[i: i + 1] = [[d + 1, v // 2],
                           [d + 1, (v + 1) // 2]]
            return red(a)
    return a

def add(a, b):
    a = deepcopy(a)
    b = deepcopy(b)
    a += b
    for i in range(len(a)):
        a[i][0] += 1
    return red(a)

def sum(l):
    return reduce(add, l)

def mag(a):
    i = 0
    def rec(d):
        nonlocal i
        if a[i][0] == d:
            x = a[i][1]
            i += 1
        else:
            x = rec(d + 1)
        if a[i][0] == d:
            y = a[i][1]
            i += 1
        else:
            y = rec(d + 1)
        return 3 * x + 2 * y
    return rec(0)

l = list(map(ld, open('18.txt').read()[:-1].split('\n')))
res = mag(sum(l))
print(res) # 1

res = max(mag(add(l[i], l[j]))
          for i in range(len(l)) for j in range(len(l))
          if i != j)
print(res) # 2
