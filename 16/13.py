k=int(open('13.txt').read().strip())

def w(x,y):
    z=x*x+3*x+2*x*y+y+y*y
    z+=k
    return z.bit_count()&1

q=[(0,1,1)]
v={(1,1)}
a=[0]*2
while q:
    t,i,j=q.pop(0)
    if t<=50:
        a[1]+=1
    if (i,j)==(31,39):
        a[0]=t
    if a[0] and t>50:
        print(*a,sep='\n')
        exit()
    for i,j in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
        if i<0 or j<0:
            continue
        if w(i,j):
            continue
        if (i,j) in v:
            continue
        v.add((i,j))
        q.append((t+1,i,j))
raise
