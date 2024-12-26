from collections import deque
m=[tuple(map(int,x.split(','))) for x in open('18.txt').read().strip().split('\n')];n=71
def f(k):
    q=deque([(0,0,0)]);v={(0,0)};mk={m[i] for i in range(k)}
    while q:
        i,j,d=q.popleft()
        if (i,j)==(n-1,n-1):return d
        for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
            if i+di not in range(n) or j+dj not in range(n):continue
            if (i+di,j+dj) in mk:continue
            if (i+di,j+dj) in v:continue
            v.add((i+di,j+dj))
            q.append((i+di,j+dj,d+1))
    return 0
print(f(1024))
for k in range(1024,len(m)):
    if not f(k):print(','.join(map(str,m[k-1])));break
