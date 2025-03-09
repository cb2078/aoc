m=[list(map(int,x.split())) for x in open('03.txt').read().strip().split('\n')]
f=lambda x,y,z:(lambda x,y,z:x+y>z)(*sorted([x,y,z]))
print(sum(f(x,y,z) for x,y,z in m))
print(sum(f(m[i][j],m[i+1][j],m[i+2][j]) for i in range(0,len(m),3) for j in range(3)))
