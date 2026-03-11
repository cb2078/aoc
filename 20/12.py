p=0;r=1
for s in open('12.txt').read().strip().split('\n'):
	x,y=s[0],int(s[1:])
	if x in 'NSEW':
		p+={'N':1j,'S':-1j,'E':1,'W':-1}[x]*y
	elif x in 'LR':
		r*=[-1j,1j][x=='L']**(y//90)
	elif x=='F':
		p+=r*y
	else:
		raise
print('%0.f'%(abs(p.real)+abs(p.imag)))

p=0;r=1;w=10+1j
for s in open('12.txt').read().strip().split('\n'):
	x,y=s[0],int(s[1:])
	if x in 'NSEW':
		w+={'N':1j,'S':-1j,'E':1,'W':-1}[x]*y
	elif x in 'LR':
		w*=[-1j,1j][x=='L']**(y//90)
	elif x=='F':
		p+=w*y
	else:
		raise
print('%0.f'%(abs(p.real)+abs(p.imag)))

