r = open('17.txt').read()[13:-1].split(', ')
r = [list(map(int, s[2:].split('..'))) for s in r]
r = [(x, y + 1) for x, y in r]

# 1
ymax = -r[1][0] - 1
print(((ymax + 1) * ymax) // 2)

# 2
xmax = r[0][1] - 1
xmin = 0
while (xmin + 1) * xmin // 2 < r[0][0]:
    xmin += 1

def t(dx, dy):
    x = y = 0
    while x < r[0][1] and y >= r[1][0]:
        if r[0][0] <= x < r[0][1] and r[1][0] <= y < r[1][1]:
            return True
        x += dx
        y += dy
        dx = max(0, dx - 1)
        dy -= 1
    return False

res = sum(t(x, y)
          for x in range(xmin, xmax + 1)
          for y in range(r[1][0], ymax + 1))
print(res)
