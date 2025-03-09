r=[]
for s in open('20.txt').read().strip().split('\n'):
    a,b=map(int,s.split('-'))
    for i in range(len(r))[::-1]:
        c,d=r[i]
        if max(a,c)<=min(b,d):
            a,b=min(a,c),max(b,d)
            del r[i]
    r.append((a,b))

r.sort()
assert all(a<b<=c<d for (a,b),(c,d) in zip(r,r[1:]))

x=y=0
for (a,b),(c,d) in zip(r,r[1:]):
    if not x and b+1!=c:
        x=b+1
    y+=c-b-1
print(x)
print(y)
