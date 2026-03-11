k=list(map(int,open('25.txt').read().strip().split('\n')))
s=7
x=[1]*2
l=[0]*2
for i in range(2):
	while x[i]!=k[i]:
		x[i]*=s
		x[i]%=20201227
		l[i]+=1
x=[1]*2
for i in range(2):
	for _ in range(l[i]):
		x[i]*=k[~i]
		x[i]%=20201227
print(x[0])
