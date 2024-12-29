m={};exec(open('10.py').read(),m);h=m['h'];del m
s=open('14.txt').read().strip()
R=tuple(range(128))
m=[format(int(h(s+'-'+str(i)),16),'0128b') for i in R]
print(sum(s.count('1') for s in m))
v=[(i,j) for i in R for j in R if m[i][j]=='1']
r=0
while v:
    q=[v.pop()]
    r+=1
    while q:
        i,j=q.pop(0)
        for i,j in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if i not in R or j not in R:
                continue
            if m[i][j]!='1':
                continue
            if (i,j) not in v:
                continue
            v.remove((i,j))
            q.append((i,j))
print(r) # 1087<
