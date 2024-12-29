p=open('10.txt').read().strip()
n=256

def f(L):
    h=list(range(n))
    i=0
    s=0
    def swp(i,j):
        i,j=i%n,j%n
        h[i],h[j]=h[j],h[i]
    for l in L:
        for j in range(l//2):
            swp(i+j,i+l-1-j)
        i=i+l+s
        s+=1
    return h
h=f(map(int,p.split(',')))
print(h[0]*h[1]) # <41820

def h(s):
    L=list(map(ord,s))+[17,31,73,47,23]
    h=f(L*64)
    d=[]
    for i in range(0,n,16):
        x=h[i]
        for j in range(1,16):
            x^=h[i+j]
        d.append(format(x,'02x'))
    return ''.join(d)
print(h(p))
