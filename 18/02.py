import string
f=open('02.txt').read().strip().split('\n');n2=0;n3=0;
h=lambda x:[any(x.count(c)==n for c in string.ascii_lowercase) for n in (2, 3)]
for s in f:x,y=h(s);n2+=x;n3+=y
print(n2*n3) # p1
m=lambda s,S:len(s)==sum(s[i]==S[i] for i in range(len(s)))+1
for i in range(len(f)):
    for j in range(i+1,len(f)):
        if m(f[i],f[j]):
            for k in range(len(f[i])):
                if f[i][k]!=f[j][k]:
                    print(f[i][:k]+f[i+1][k+1:]) # p2
                    exit(0)
