a=b=0
for s in open('02.txt').read().strip().split('\n'):
	w=s.split();x,y=map(int,w[0].split('-'));c=w[1][0];z=w[-1];
	a+=x<=z.count(c)<=y
	b+=(z[x-1],z[y-1]).count(c)==1
print(a,b,sep='\n')
