for m in ['123','456','789'],['  1  ',' 234 ','56789',' ABC ','  D  ']:
    n=len(m)
    i=j=(n-1)//2
    d={'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}
    for s in open('02.txt').read().strip().split('\n'):
        for c in s:
            di,dj=d[c]
            if di and i+di in range(n) and m[i+di][j]!=' ':
                i+=di
            if dj and j+dj in range(n) and m[i][j+dj]!=' ':
                j+=dj
        print(m[i][j],end='')
    print()
