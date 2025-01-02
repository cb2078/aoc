import re
w=r'.*?';d=r'(\d+)';s='[%s]'%re.sub(w+d+w+d+w+d+w+'\n',r'(\1,\2,\3), ',open('14.txt').read())[:-2];p=eval(s);n=len(p)
T=2503
from itertools import accumulate as a
m=[[*a(t%(x+y)<x and v for t in range(T))] for v,x,y in p]
x=[max(m[i][j] for i in range(n)) for j in range(T)]
print(x[-1],max(sum(m[i][j]==x[j] for j in range(T)) for i in range(n)),sep='\n')
