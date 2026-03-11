l=list(map(int,open('09.txt').read().strip().split('\n')))
n=len(l)

def f(i):
	for j in range(i-25,i):
		for k in range(j+1,i):
			if l[j]+l[k]==l[i]:
				return True
	return False

i=next(i for i in range(25,n) if not f(i))
print(x:=l[i])

	for i in range(n):
	for j in range(i+2,n):
		y=sum(l[i:j])
		if y==x:
			print(min(l[i:j])+max(l[i:j]));quit()
		elif y>x:
			break
