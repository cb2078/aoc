from hashlib import md5
q=[(0,0,open('17.txt').read().strip())]
d=(-1,0),(1,0),(0,-1),(0,1)
s='UDLR'
l=[]
while q:
    i,j,h=q.pop(0)
    if i==3 and j==3:
        l.append(h[8:])
        continue
    for k,c in enumerate(md5(h.encode()).hexdigest()[:4]):
        if c not in 'bcdef':
            continue
        di,dj=d[k]
        if i+di not in range(4) or j+dj not in range(4):
            continue
        q.append((i+di,j+dj,h+s[k]))
print(l[0],len(l[-1]))
