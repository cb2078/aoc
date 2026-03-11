with open('7.txt') as f:
    p = list(map(int, f.read()[:-1].split(',')))

p1 = lambda x: x
p2 = lambda x: (x + 1) * x / 2

res = min(sum(p2(abs(c - x)) for c in p)
          for x in range(min(p), max(p)))
print(res)
