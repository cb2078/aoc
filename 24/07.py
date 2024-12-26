p=open('07.txt').read().strip().split('\n');p=[list(map(int,x.replace(': ',' ').split())) for x in p]
o=[lambda x,y:x+y,lambda x,y:x*y]
f=lambda x,y,z:any(f(g(x,y[0]),y[1:],z) for g in o) if y else x==z
print(sum(x[0] for x in p if f(x[1],x[2:],x[0])))
o.append(lambda x,y:int(str(x)+str(y)))
print(sum(x[0] for x in p if f(x[1],x[2:],x[0])))
