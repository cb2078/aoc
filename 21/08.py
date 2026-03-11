with open('8.txt') as f:
    p = f.read()[:-1].split('\n')

# 1
res = 0
for l in p:
    l = l.split(' | ')[1]
    res += sum(len(d) in (2, 4, 3, 7) for d in l.split(' '))
print(res)

#2
result = 0
for l in p:
    u, o = l.split(' | ')
    u = [set(x) for x in u.split()]
    u5 = [x for x in u if len(x) == 5]
    u6 = [x for x in u if len(x) == 6]
    n = {}
    n[1], n[4], n[7], n[8] = [[x for x in u if len(x) == y][0]
                               for y in (2, 4, 3, 7)]
    a = {}
    a['a'] = n[7] - n[1]
    a['d'] = n[4] & set.intersection(*u5) - a['a']
    a['b'] = n[4] - n[1] - a['d']
    n[0] = n[8] - a['d']
    a['g'] = set.intersection(*u5) - a['a'] - a['d']
    n[9] = n[4] | a['a'] | a['g']
    a['e'] = n[8] - n[9]
    n[3] = n[7] | a['d'] | a['g']
    n[6] = [x for x in u6 if x not in (n[0], n[9])][0] 
    a['c'] = n[8] - n[6]
    a['f'] = n[1] - a['c']
    n[2] = n[8] - a['b'] - a['f']
    n[5] = n[6] - a['e']

    o = list(map(set, o.split()))
    result += sum(k * 10 ** i for i, d in enumerate(o[::-1]) for k in n
                  if d == n[k])

print(result)
