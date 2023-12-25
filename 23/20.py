LOW, HIGH = range(2)
OFF, ON = range(2)

p = open('20.txt').read().strip().split('\n')

from dataclasses import dataclass

@dataclass
class FF:
    next: list
    state: int
    type: str

@dataclass
class C:
    next: list
    prev: dict
    type: str

@dataclass
class B:
    next: list
    type: str

g = dict()
for l in p:
    t = l[0] if l[0] in '%&' else 'broadcaster'
    l = l.split(' -> ')
    m = l[0].replace('%', '').replace('&', '')
    nxt = l[1].split(', ')
    g[m] = \
        FF(nxt, OFF, t) if t == '%' else \
        C(nxt, {}, t) if t == '&' else \
        B(nxt, t)
for m in g:
    if g[m].type == '&':
        for M in g:
            if m in g[M].next:
                g[m].prev[M] = LOW

flag = False; log = lambda *args: flag and print(*args)
from collections import deque
def step():
    c = [1, 0]
    q = deque([('broadcaster', LOW, 'button')])
    while q:
        m, s, p = q.popleft()
        if m == P and s == HIGH and 0 == d[p]:
            d[p] = i
        if m not in g:
            continue
        log(m, s, p)
        if g[m].type == '%':
            if s == HIGH:
                continue
            g[m].state ^= 1
            S = g[m].state
        elif g[m].type == '&':
            g[m].prev[p] = s
            S = LOW if all(v == HIGH for v in g[m].prev.values()) else HIGH
        else: # broadcaster
            S = LOW
        log(g[m])
        for M in g[m].next:
            q.append((M, S, m))
            c[S] += 1
            log(m, S, M)
        log()
    return c

for P in g:
    if g[P].next == ['rx']:
        break
else:
    raise AssertionError
assert g[P].type == '&'

d = {k: 0 for k in g[P].prev}
i = 0
a = b = 0
while not all(d.values()):
    i += 1
    c = step()
    a += c[0]
    b += c[1]
    if i == 1000:
        print(a * b) # p1
import math
print(math.lcm(*d.values())) # p2
