for p in 1,2:
	mem={}
	for s in open('14.txt').read().strip().split('\n'):
		if s.startswith('mask'):
			mask=s.split()[-1]
		else:
			w=s.split()
			if p==1:
				v=int(w[-1])
				for i in range(36):
					if mask[i]=='1':
						v|=1<<35-i
					elif mask[i]=='0':
						v&=~(1<<35-i)
				exec(w[0]+w[1]+str(v))
			else:
				v=format(int(w[0][4:w[0].index(']')]),'036b')
				f=lambda i=0:[''] if i>35 else [c+s for s in f(i+1) for c in '01'] if mask[i]=='X'\
					 else [('1' if mask[i]=='1' else v[i])+s for s in f(i+1)]
				for a in f():
					mem[int(a,2)]=int(w[-1])
	print(sum(mem.values()),'done')
