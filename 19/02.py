def f(x,y):
    p=[*map(int,open('02.txt').read().strip().split(','))]
    p[1:3]=x,y
    i=0
    while True:
        match p[i]:
            case 1:
                p[p[i+3]]=p[p[i+1]]+p[p[i+2]]
            case 2:
                p[p[i+3]]=p[p[i+1]]*p[p[i+2]]
            case 99:
                break
            case _:
                raise
        i+=4
    return p[0]

print(f(12,2))

from itertools import count as c
n=19690720
for i in c():
    if f(i,i)==n:
        print(100*i+i)
        quit()
    for j in range(i):
        if f(i,j)==n:
            print(100*i+j)
            quit()
        if f(j,i)==n:
            print(100*j+i)
            quit()
