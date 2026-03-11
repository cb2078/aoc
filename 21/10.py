with open('10.txt') as f:
    p = f.read()[:-1].split('\n')

start = '([{<'
end = ')]}>'
n = len(start)
m = {end[i]: start[i] for i in  range(n)}

def p1(l):
    s = []
    t = {')': 3,
         ']': 57,
         '}': 1197,
     '>': 25137}
    for c in l:
        if c in start:
            s.append(c)
        elif s[-1] == m[c]:
            s.pop()
        else:
            return t[c]
    return 0

res = sum(p1(l) for l in p)
print(res)

def p2(l):
    s = []
    t = {'(': 1,
         '[': 2,
         '{': 3,
         '<': 4}
    for c in l:
        if c in start:
            s.append(c)
        elif s[-1] == m[c]:
            s.pop()
        else:
            return 0
    tot = 0
    for c in s[::-1]:
        tot += tot * 5 + t[c]
    return tot

res = [p2(l) for l in p]
res = sorted(x for x in res if x)
res = res[len(res) // 2]
print(res)
