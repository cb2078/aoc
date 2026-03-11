o=lambda i=0:print('%2d'%(i+1),end=' ') or (print() if r[i]==0 else o(r[i]))

for p in 1,2:
	c=[int(x)-1 for x in open('23.txt').read().strip()]
	i=c[0]
	n=len(c)
	r=[c[(c.index(i)+1)%n] for i in range(n)]
	if p==2:
		n=10**6	
		r+=list(range(10,n))+[c[0]]
		r[c[-1]]=9

	for _ in range(100 if p==1 else 10**7):
		j=i
		a=[None]*3
		for k in range(3):
			j=r[j]
			a[k]=j
		j=i
		while True:
			j-=1;j%=n
			if j not in a:
				break
		# i, a[0], a[1], a[2], x, ..., j, y
		# v
		# i, x, ..., j, a[0], a[1], a[2], y
		x=r[a[2]]
		y=r[j]
		r[i]=x
		r[j]=a[0]
		r[a[2]]=y
		i=r[i]

	if p==1:
		i=r[0]
		while i:
			print(1+i,end='');i=r[i]
		print()
	else:
		x,y=r[0]+1,r[r[0]]+1;print(x*y)
