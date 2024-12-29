import re
s=open('25.txt').read().strip()+'\n'
k=int(re.search(r'\d+',s).group())
r=re.findall(r'(\S+)\.\n',s)[2:]
d={'0':0,'1':1,'left':-1,'right':1,'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}
m=[[[d[s] for s in r[j:j+3]] for j in range(i,i+6,3)] for i in range(0,len(r),6)]
from collections import defaultdict
t=defaultdict(int)

i=0
s=0
for _ in range(k):
    v,j,s=m[s][t[i]]
    t[i]=v
    i+=j
print(sum(t.values()))
