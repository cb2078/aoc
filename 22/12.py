p=open('12.txt').read().strip().split('\n')
h,w=len(p),len(p[0])
(si,sj),(ei,ej)=([(i,j) for i in range(h) for j in range(w) if p[i][j]==c][0] for c in 'SE')
p=[list(map(ord,x)) for x in p]
p[si][sj]=ord('a')
p[ei][ej]=ord('z')

s=[(si,sj,0)]
v=set()
while s:
    (i,j,n),*s=s
    if (i,j) in v:
        continue
    v|={(i,j)}
    if (i,j)==(ei,ej):
        print(n) # 1
        break
    for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
        if i+di in range(h) and j+dj in range(w) and p[i+di][j+dj]-p[i][j]<=1:
            s+=[(i+di,j+dj,n+1)]

s=[(ei,ej,0)]
v=set()
while s:
    (i,j,n),*s=s
    if (i,j) in v:
        continue
    v|={(i,j)}
    if p[i][j]==ord('a'):
        print(n) # 2
        break
    for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
        if i+di in range(h) and j+dj in range(w) and p[i+di][j+dj]-p[i][j]>=-1:
            s+=[(i+di,j+dj,n+1)]
