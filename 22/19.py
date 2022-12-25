import re

res = ['ore', 'clay', 'obsidian', 'geode']
parse = lambda d: [int(d[r]) if r in d else 0 for r in res]

p = open('19.txt').read().strip().split('\n')
p = [[parse(dict(z[::-1] for z in re.findall(r'(\d+) (\w+)', y))) for y in x.split(' Each ')[1:]] for x in p]

t0 = 24
ans = 0
for i, bp in enumerate(p):
    print(i)
    ore_max = max(bp[i][0] for i in range(4))
    dp = {}
    def solve(t, res, rob):
        can_build = lambda i: all(bp[i][j] <= res[j] for j in range(4))
        build = lambda i: solve(t - 1,
                                [res[j] + rob[j] - bp[i][j] for j in range(4)],
                                [rob[j] + (j == i) for j in range(4)])
        k = (t, tuple(res), tuple(rob)) 
        if k in dp:
            return dp[k]
        if t == 0:
            return res[3]
        for i in (3, 2):
            if can_build(i):
                x = build(i)
                break
        else:
            x = solve(t - 1, [res[j] + rob[j] for j in range(4)], rob)
            for i in (0, 1):
                if can_build(i):
                    x = max(x, build(i))
        dp[k] = x
        return x
    ans += (1 + i) * solve(t0, [0 for _ in range(4)], [1] + [0 for _ in range(3)])
print(ans)
