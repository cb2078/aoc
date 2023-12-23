p = [x.split('\n') for x in open('13.txt').read().strip().split('\n\n')]

def transpose(m):
    return list(map(list, zip(*m)))

def ref(m):
    for i in range(len(m) - 1):
        if all(m[i - k] == m[i + 1 + k] for k in range(min(i + 1, len(m) - (i + 1)))):
            return 100 * (i + 1)
    return ref(transpose(m)) // 100

def ref2(m):
    for i in range(len(m) - 1):
        r = min(i + 1, len(m) - (i + 1))
        s = sum(m[i - k][j] == m[i + 1 + k][j] for k in range(r) for j in range(len(m[0])))
        if s + 1 == r * len(m[0]):
            return 100 * (i + 1)
    return ref2(transpose(m)) // 100

print(sum(map(ref, p))) # p1
print(sum(map(ref2, p))) # p2
