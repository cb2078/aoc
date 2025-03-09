d=[x.replace('[',']').split(']') for x in open('07.txt').read().strip().split('\n')]
def f(l):
    b=[any(x[i]==x[i+3] and x[i+1]==x[i+2] and x[i]!=x[i+1] for i in range(len(x)-3)) for x in l]
    return any(b[::2]) and not any(b[1::2])
def g(l):
    a,b=[{''.join(s[i:i+3]) for s in l[o::2] for i in range(len(s)-2) if s[i]==s[i+2] and s[i]!=s[i+1]} for o in [0,1]]
    return any(x[0]==y[1] and x[1]==y[0] for x in a for y in b)
for h in f,g:print(sum(map(h,d)))
