def f():
	global i
	if s[i]=='(':
		i+=1
		x=g()
	else:
		x=int(s[i])
	i+=1
	return x

def g(j=0):
	global i
	h=lambda:g(j+1) if j+1<len(p) else f()
	x=h()
	while i<len(s):
		if s[i] not in p[j]:
			break
		o=s[i]
		i+=1
		y=h()
		x=eval('x'+o+'y')
	return x

for p in ['+*'],['*','+']:
	a=0
	for s in open('18.txt').read().strip().split('\n'):
		# print(s,'=',end=' ')
		s=s.replace(' ','')
		i=0
		x=g()
		a+=x
		# print(x)
	print(a)
