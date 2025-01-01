x=[ord(c)-ord('a') for c in open('10.txt').read().strip()]

iol=[ord(c)-ord('a') for c in 'iol']
f1=lambda x:any(x[i]+1==x[i+1] and x[i+1]+1==x[i+2] for i in range(len(x)-2))
f2=lambda x:all(x[i] not in iol for i in range(len(x)))
f3=lambda x:any(x[i]==x[i+1] and x[j]==x[j+1] for i in range(len(x)-1) for j in range(i+2,len(x)-1))
f=lambda x:f1(x) and f3(x)

def g(x):
    for i in range(len(x))[::-1]:
        if x[i]<25:x[i]+=[1,2][x[i]+1 in iol];return x
        x[i]=0
    raise

def h(x):
    while not f(x):x=g(x)
    return x

o=lambda x:print(''.join(chr(x[i]+ord('a')) for i in range(len(x))))
x=h(x);o(x);y=h(g(x[:]));o(y)
