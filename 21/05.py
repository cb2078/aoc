p = open('5.txt').read()[:-1].split('\n')
print(p)
p = [[list(map(int, x.split(','))) for x in s.split(' -> ')] for s in p]
p0 = [pair for pair in p
     if pair[0][0] == pair[1][0] or pair[0][1] == pair[1][1]]
p1 = [pair for pair in p
      if not (pair[0][0] == pair[1][0] or pair[0][1] == pair[1][1])]
print(p0)
print(p1)

x_max = y_max = 0
for pair in p:
    x_max = max(x_max, max(pair[0][0], pair[1][0]))
    y_max = max(y_max, max(pair[0][1], pair[1][1]))
print(x_max, y_max)

g = [[0 for _ in range(x_max + 1)] for _ in range(y_max + 1)]

for pair in p0:
    x_min = min(pair[0][0], pair[1][0])
    x_max = max(pair[0][0], pair[1][0]) + 1
    y_min = min(pair[0][1], pair[1][1])
    y_max = max(pair[0][1], pair[1][1]) + 1
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            g[y][x] += 1

for pair in p1:
    c = pair[0][::]
    x_dir = 1 if pair[0][0] < pair[1][0] else -1
    y_dir = 1 if pair[0][1] < pair[1][1] else -1
    x_min = min(pair[0][0], pair[1][0])
    x_max = max(pair[0][0], pair[1][0]) + 1
    for _ in range(x_min, x_max):
        g[c[1]][c[0]] += 1
        c[0] += x_dir
        c[1] += y_dir
    
for r in g:
    print(''.join(str(x) if x != 0 else '.' for x in r))
    # print(''.join('_#'[x >= 2] for x in r))
result = sum(x >= 2 for y in g for x in y)
print(result)
