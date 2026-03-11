f=open('09.txt').read().strip().split();p,n=[int(f[i]) for i in [0,6]]
def p1(p,n):
    l=[0];j=0;s=[0]*p
    for i in range(1,1+n):
        if i%23:j=(j+2)%len(l);l.insert(j,i)
        else:s[i%p]+=i+l[(j-7)%len(l)];J=j if (j-7)%len(l)>j else j-1;del l[(j-7)%len(l)];j=(J-6)%len(l)
        # print('[%02d]'%((i-1)%p+1),''.join(('(%02d)' if k==j else ' %02d ') % (l[k]) for k in range(len(l))))
    return max(s)
print(p1(p,n)) # p1
class N:
    def __init__(s,v,l=None,r=None):
        assert bool(l)==bool(r)
        if l:s.l=l;l.r=s
        else:s.l=s
        if r:s.r=r;r.l=s
        else:s.r=s
        s.v=v
    def __iter__(s):
        yield s
        n=s.r
        while n!=s:
            yield n
            n=n.r
    def __getitem__(s,i):
        n=s
        if i>0:
            for _ in range(i):n=n.r
        else:
            for _ in range(-i):n=n.l
        return n
    def insert(s,i,v):
        n=s[i]
        return N(v,n.l,n)
    def remove(s,i):
        assert i
        n=s[i];n.l.r=n.r;n.r.l=n.l
    __repr__=lambda s:s.v.__repr__()
    __str__=lambda s:s.v.__str__()
# n0=N(0);n=n0
# for i in range(22):n=n.insert(2,i+1)
# print(list(n0));n.remove(-7);print(list(n0),n[-6])
def p2(p,k):
    n=n0=N(0);s=[0]*p
    for i in range(1,1+k):
        if i%23:n=n.insert(2,i)
        else:s[i%p]+=i+n[-7].v;n.remove(-7);n=n[-6]
        # print(list(n0),n.v)
    return max(s)
print(p2(p,100*n)) # p2
