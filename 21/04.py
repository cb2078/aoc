pi=open('4.txt').read()[:-1].split('\n\n')
N,*B=pi
N=list(map(int,N.split(',')))
B=[[list(map(int,r.split())) for r in b.split('\n')] for b in B]
c=0
m=[[[0 for _ in range(5)] for _ in range(5)] for b in B]
for n in N:
    for k,b in enumerate(B):
        for i in range(5):
            for j in range(5):
                if b[i][j]==n:
                    m[k][i][j]=1
        for i in range(5):
            if all(m[k][i][j] for j in range(5)) or all(m[k][j][i] for j in range(5)):
                sum=0
                for i in range(5):
                    for j in range(5):
                        if not m[k][i][j]:
                            sum+=b[i][j]
                print(sum*n)
                exit()
