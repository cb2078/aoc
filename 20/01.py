l=list(map(int,open('01.txt').read().strip().split('\n')));e=*enumerate(l),
x,y=next((x,y) for i,x in e for j,y in e if i<j and x+y==2020);print(x*y)
x,y,z=next((x,y,z) for i,x in e for j,y in e for k,z in e if i<j<k and x+y+z==2020);print(x*y*z)
