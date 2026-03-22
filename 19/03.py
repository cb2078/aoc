M=[{},{}]
d={'U':1j,'D':-1j,'L':-1,'R':1}
W=[x.split(',') for x in open('03.txt').read().strip().split('\n')]
for m,w in zip(M,W):
    z=0j
    m[z]=0
    t=1
    for s in w:
        for _ in range(int(s[1:])):
            z+=d[s[0]]
            if z not in m:
                m[z]=t
            t+=1
i=M[0].keys()&M[1].keys()
print('%.0f'%min(abs(z.real)+abs(z.imag) for z in i if z))
print(min(M[0][z]+M[1][z] for z in i if z))
