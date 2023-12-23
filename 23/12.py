p = [l.split(' ') for  l in open('12.txt').read().split('\n')[:-1]]
p = [(x, tuple(map(int, y.split(',')))) for x, y in p]
p = [('?'.join([s] * 5), g * 5) for s, g in p]

dp = {}
def countDP(s, g):
    if (s, g) not in dp:
        dp[s, g] = count(s, g)
    return dp[s, g]
def count(s, g):
    if len(g) == 0:
        return s.count('#') == 0
    if g[0] >= len(s):
        return 0
    forward = countDP(s[1:], g) if s[0] in '.?' else 0
    group = countDP(s[1 + g[0]:], g[1:]) if '.' not in s[:g[0]] and s[g[0]] != '#' else 0
    return forward + group

print(sum(count(s + '...', g) for s, g in p)) # p2
