p=open('05.txt').read().strip().split('\n\n')
r,u=[[list(map(int,x.split(c))) for x in p[i].split('\n')] for i,c in enumerate('|,')]#;print(r);print(u)
c=lambda x:not any([x[i+1],x[i]] in r for i in range(len(x)-1))
print(sum(x[len(x)//2] for x in u if c(x))) # p1

def s(x):
    while True:
        for i in range(len(x)-1):
            if [x[i+1],x[i]] in r:
                x[i:i+2]=[x[i+1],x[i]]
                break
        else:
            return x

print(sum(s(x)[len(x)//2] for x in u if not c(x))) # p2

# n=1+max(y for x in r for y in x)
# d=[[0 for _ in range(n)] for _ in range(n)]
# od=lambda:print('\n'.join(''.join(' #'[d[i][j]] for j in range(n)) for i in range(n)))
# for j,i in r:d[i][j]=1
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             d[i][j]=d[i][j] or d[i][k] and d[k][j]
# c=lambda x:all(0==d[x[i]][x[j]] for i in range(len(x)) for j in range(1+i,len(x)))
# # print(sum(x[len(x)//2] if c(x) else 0 for x in u)) # p1
# print(x:=u[6])
# print([d[x[i]][x[j]] for i in range(len(x)) for j in range(1+i,len(x))])
