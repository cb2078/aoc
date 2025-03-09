import re
r=[re.split(r'-|\[',s[:-1]) for s in open('04.txt').read().strip().split('\n')]
def f(x):s=''.join(x[:-2]);return sorted(set(s),key=lambda c:(-s.count(c),c))[:5]
c=lambda x:''.join(f(x))==x[-1]
# for i in range(len(r)):print(r[i],c(r[i]),sep='\n',end='\n\n')
r=[x for x in r if c(x)]
print(sum(int(x[-2]) for x in r))
for x in r:
    n=int(x[-2])
    m=' '.join(''.join(chr((ord(c)-ord('a')+n)%26+ord('a')) for c in s) for s in x[:-2])
    if 'north' in m:
        print(x[-2])
