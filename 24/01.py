p=open('01.txt').read().strip().split('\n')
l,r=map(sorted,zip(*[map(int,l.split('   ')) for l in p]))
print(sum(abs(x-y) for x,y in zip(l,r))) # p1
print(sum(x*r.count(x) for x in l)) # p2
