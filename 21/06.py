p = list(map(int, open('6.txt').read().split(',')))
a = [p.count(i) for i in range(8 + 1)]

# for _ in range(18):
# for _ in range(80):
for _ in range(256):
    t = a[0]
    a[:8] = a[1:]
    a[8] = t
    a[6] += t

print(sum(a))
