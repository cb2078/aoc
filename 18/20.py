s=open('20.txt').read().strip()
m=set();c='NSEW';d=[-1j,1j,1,-1];v=set()

def f(i=1,z=0):
    if (i,z) in v:
        return
    v.add((i,z))
    while True:
        if s[i]=='$':
            break
        elif s[i] in c:
            while s[i] in c:
                w=dict(zip(c,d))[s[i]]
                m.add(z*2+w)
                z+=w
                i+=1
        elif s[i]=='(':
            f(i+1,z)
            n=0
            i+=1
            while n>0 or s[i]!=')':
                if n==0 and s[i]=='|':
                    f(i+1,z)
                n+=(s[i]=='(')-(s[i]==')')
                i+=1
            return
        elif s[i]=='|':
            n=0
            while n>0 or s[i]!=')':
                n+=(s[i]=='(')-(s[i]==')')
                i+=1
        elif s[i]==')':
            i+=1
        else:
            raise
f()

h=lambda z:z.real%2==1 or z.imag%2==1;g=lambda z:h(z) and z not in m
# print('\n'.join(''.join('.#'[g(complex(i,j))] for j in range(-10,10)) for i in range(-10,10)))
r=[0,0];q=[0];v=set(q)
while True:
    Q=[]
    while q:
        z=q.pop()
        if not h(z) and r[0]//2>=1000:
            r[1]+=1
        for w in d:
            if not g(z+w) and z+w not in v:
                v.add(z+w);Q.append(z+w)
    if not Q:
        break
    q=Q
    r[0]+=1
assert r[0]%2==0
print(r[0]//2,r[1],sep='\n')
