l = list(map(int,open('20.txt').read().strip().split('\n')))

def f(l, t):
    n = len(l)
    p = list(range(n)) # p[index] = id
    for _ in range(t):
        for i in range(n):
            k = p.index(i)
            j = p.pop(k)
            p.insert((l[i] + k) % (n - 1), j)
    l = [l[i] for i in p]
    i = l.index(0)
    return sum(l[(i + j) % n] for j in (1000, 2000, 3000))

print(f(l, 1)) # 1
print(f([x * 811589153 for x in l], 10)) # 2
