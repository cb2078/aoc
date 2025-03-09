l=[*open('01.txt').read().strip().split(', ')]

d=1j;p=0
for s in l:
    d*=[1j,-1j][s[0]=='R']
    p+=int(s[1:])*d
print('%d'%(abs(p.real)+abs(p.imag)))

d=1j;p=0
i=0
v={p}
while True:
    s=l[i%len(l)]
    d*=[1j,-1j][s[0]=='R']
    for _ in range(int(s[1:])):
        p+=d
        if p in v:
            print('%d'%(abs(p.real)+abs(p.imag)))
            exit()
        v.add(p)
    i+=1
