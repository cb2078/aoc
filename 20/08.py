p=[(lambda x,y:[x,int(y)])(*s.split()) for s in open('08.txt').read().strip().split('\n')]

def r():
	v=set()
	a=0
	i=0
	while i not in v:
		x,y=p[i]
		v.add(i)
		match x:
			case 'acc':
				a+=y
			case 'jmp':
				i+=y-1
			case 'nop':
				pass
			case _:
				raise
		i+=1
		if i==len(p):
			return True,a
	return False,a

print(r()[1])

def s(j):
	match p[j][0]:
		case 'acc':
			pass
		case 'jmp':
			p[j][0]='nop'
		case 'nop':
			p[j][0]='jmp'
		case _:
			raise

for j in range(len(p)):
	s(j)
	b,a=r()
	if b:
		print(a)
		quit()
	s(j)
