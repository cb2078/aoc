w=[*map(int,open('24.txt').read().strip().split('\n'))]
for k in 3,4:
    r=float('inf'),float('inf')
    def f(n=sum(w)//k,i=0,v=0,g=0,p=1):
        global r
        if g==0 and (t:=(v.bit_count(),p))>r:
            return
        if n==0:
            if g==0:
                try:
                    f(v=v,g=g+1)
                except Exception:
                    r=min(r,t)
            elif g<k-2:
                f(v=v,g=g+1)
            else:
                raise Exception
        if n>0 and i<len(w):
            f(n,i+1,v,g,p)
            if ~v>>i&1:
                f(n-w[i],i+1,v|1<<i,g,p*w[i])
    f()
    print(r[1])
