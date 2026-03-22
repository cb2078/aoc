a=*map(int,open('01.txt').read().strip().split('\n')),
f=lambda x:x//3-2
g=lambda x:f(x)+g(f(x)) if x>0 else x
for h in [f,g]:print(sum(map(h,a)))
