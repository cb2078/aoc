g=iter(open('19.txt').read().strip().split('\n'))

def p(v):
	if '|' in v:
		return [x for [x] in map(p,v.split(' | '))]
	if ' ' in v:
		return [[x for [[x]] in map(p,v.split())]]
	return [[int(v)]]
r={}
while s:=next(g):
	k,v=s.split(': ')
	r[eval(k)]=eval(v) if '"' in v else p(v)

def f(s,i=0,k=0):
	if type(r[k])==str:
		if s[i]==r[k]:
			yield i+1
		return
	for t in r[k]:
		J=[i]
		for x in t:
			J=[y for j in J if j<len(s) for y in f(s,j,x)]
		yield from J

l=list(g)
for p in 1,2:
	if p==2:
		r[8].append([42,8])
		r[11].append([42,11,31])
	print(sum(any(x==len(s) for x in f(s)) for s in l))
