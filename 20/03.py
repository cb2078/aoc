m=open('03.txt').read().strip().split('\n');n=len(m)

a=[]
for dj,di in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
	i=j=0;a.append(0)
	while i<n:a[-1]+=m[i][j]=='#';i+=di;j+=dj;j%=len(m[0])
from math import prod;print(a[1],prod(a),sep='\n')

