f=open('04.txt').read().strip().split('\n');f.sort()
def gi(s,b,e):s=s[s.find(b)+1:];return int(s[:s.find(e)])
d={};i=0
while i<len(f):
    k=gi(f[i],'#',' ')
    if k not in d:d[k]=[0]*60
    i+=1
    while i<len(f) and 'Guard' not in f[i]:
        if 'falls asleep' in f[i]:b=gi(f[i],':',']')
        elif 'wakes up' in f[i]:
            e=gi(f[i],':',']')
            for j in range(b,e):d[k][j]+=1
        else:raise
        i+=1
print('     '+''.join('%2d ' % i for i in range(60))+'\n'+'\n'.join('%4d ' % k+''.join('%2d ' % d[k][i] for i in range(60))for k in d))
k=max(d.keys(),key=lambda k:sum(d[k]));i=max(range(60),key=lambda i:d[k][i]);print(k*i) # p1
mk=mi=None
for k in d:
    for i in range(60):
        if mk is None or d[k][i]>d[mk][mi]:mi=i;mk=k
print(mk*mi) # p2
