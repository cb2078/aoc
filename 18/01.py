l=list(map(int,open('01.txt').read().strip().split('\n')))
print(sum(l))
r=0;i=0;s=set();m=100000
while r not in s:s.add(r);r+=l[i%len(l)];i+=1;m=min(m,r)
print(r,m)
