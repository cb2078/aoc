with open('11.txt') as f:
    p = [list(map(int, s)) for s in f.read()[:-1].split("\n")]
    w = len(p)

def light():
    h = [[False for _ in range(w)] for _ in range(w)]
    
    def flash(i, j):
        if i not in range(w) or j not in range(w) or h[i][j]:
            return
        p[i][j] += 1
        if p[i][j] > 9:
            h[i][j] = True505
            flash(i - 1, j)
            flash(i - 1, j - 1)
            flash(i - 1, j + 1)
            # flash(i, j)
            flash(i, j - 1)
            flash(i, j + 1)
            flash(i + 1, j)
            flash(i + 1, j - 1)
            flash(i + 1, j + 1)
    
    res = 0
    for i in range(w):
        for j in range(w):
            p[i][j] += 1
            if p[i][j] > 9:
                flash(i, j)
    for i in range(w):
        for j in range(w):
            if p[i][j] > 9:
                p[i][j] = 0
                res += 1
    return res

# # 1
# print(sum(light() for _ in range(100)))

# 2
n = 1
while light() != w ** 2:
    n += 1
print(n)

# print('\n'.join(''.join(map(str, r)) for r in p))
