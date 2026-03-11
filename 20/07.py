d={}
for s in open('07.txt').read().strip().split('\n'):
	x=s[:-1].replace('bags','bag').replace(' bag','').split(' contain ')
	d[x[0]]=[] if x[1]=='no other' else [(int(y[0]),y[2:]) for y in x[1].split(', ')]

f=lambda k:any(y=='shiny gold' for x,y in d[k]) or any(f(y) for x,y in d[k])
print(sum(map(f,d)))

g=lambda k:sum(x+x*g(y) for x,y in d[k])
print(g('shiny gold'))
