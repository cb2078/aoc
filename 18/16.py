os='addr addi mulr muli banr bani borr bori setr seti gtir gtri gtrr eqir eqri eqrr'.split();on=len(os)
# print({w[:-2 if w[2] in 'ri' else -1]:'+' for w in os})
d={'add': '+', 'mul': '*', 'ban': '&', 'bo': '|', 'set': '=', 'gt': '>', 'eq': '=='}
for k,v in d.items():s=f'def {k}(a,b,c):r[c]=a'+('' if k=='set' else f'{v}b');exec(s)#;print(s)
for o in os:
    b=o[-1];i=[-1,-2][o[-2] in 'ri'];a=o[-2] if i==-2 else o[-1] if 'set' in o else 'r'
    s=f'def {o}(a,b,c):{o[:i]}({'a' if a=='i' else 'r[a]'},{'b' if b=='i' else 'r[b]'},c)';exec(s)#;print(s)
xs,p=open('16.txt').read().strip().split('\n\n\n');p=[list(map(int,l.split())) for l in p.strip().split('\n')]
xs=xs.split('\n\n');xs=[s.split('\n') for s in xs]
for x in xs:
    for i in [0,2]:x[i]=x[i].split(' [')[-1][:-1].replace(', ',' ')
    for i in range(3):x[i]=list(map(int,x[i].split()))
def t(x,o):global r;r=x[0].copy();eval(o)(*x[1][1:]);return r==x[2]
T=lambda x:3<=sum(t(x,o) for o in os);print(sum(T(x) for x in xs)) # p1

I=[{o for o in os if all(t(x,o) for x in xs if x[1][0]==i)} for i in range(on)]#;print(*I,sep='\n')
while True:
    r={min(s) for s in I if 1==len(s)}
    if len(r)==on:break
    for s in I:
        if len(s)>1:s.difference_update(r)
    # print(*I,sep='\n',end='\n\n')
I=[l.pop() for l in I];r=[0]*4
for x in p:eval(I[x[0]])(*x[1:])
print(r[0]) # p2
