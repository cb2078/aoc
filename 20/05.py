a=[]
for s in open('05.txt').read().strip().split('\n'):
	a.append(int(s.replace('F','0').replace('B','1').replace('L','0').replace('R','1'),2))
a.sort()
print(a[-1])
x=next(x for x,y in zip(a,a[1:]) if y-x==2);print(x+1)
