p=open('05.txt').read().rstrip().split('\n\n')
crates=p[0].split('\n')[:-1]
crates=[''.join(crate[i].strip() for crate in crates) for i in range(1, len(crates[0]), 4)]
import re
inst=[tuple(map(int,re.findall(r'\d+', i))) for i in p[1].split('\n')]

for i in inst:
    n, x, y = i
    x -= 1
    y -= 1
    # crates[x], crates[y] = crates[x][n:], crates[x][:n][::-1] + crates[y] # 1
    crates[x], crates[y] = crates[x][n:], crates[x][:n] + crates[y] # 2

print(''.join(x[0] for x in crates))
