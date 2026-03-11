s,R=open('12.txt').read().strip().split('\n\n');
n=10;s='.'*n+s.split()[-1]+'.'*150;s0=s
R=[r.split() for r in R.split('\n')];R={r[0]:r[2] for r in R}
def f(s):
    S=[]
    for i in range(len(s)):
        ss=''.join(s[i+j] for j in range(-2,3) if i+j in range(len(s)))
        S.append(R[ss] if ss in R else '.' if len(ss)!=5 else '.')
    return ''.join(S)
def os(s):i=s.index('#')-2;print(s[i:min(len(s),i+180)])
def c(s,n):return sum(i-n for i in range(len(s)) if s[i]=='#')
for i in range(20):s=f(s)
print(c(s,n)) # p1
s=s0;x=c(s,n)
for i in range(1,1000000000):
    s=f(s);h=s.index('#');y=c(s,h);os(s)
    if y==x:break
    x=y
print(s.count('#')*(h-n-i+50000000000)+x) # p2
