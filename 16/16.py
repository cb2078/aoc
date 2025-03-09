for n in 272,35651584:
    a=[*map(int,open('16.txt').read().strip())]
    while len(a)<n:
        b=a[::-1]
        b=[1-x for x in b]
        a=a+[0]+b
    while True:
        a=[a[i]==a[i+1] for i in range(0,min(n,len(a))-1,2)]
        if len(a)&1:
            break
    print(''.join(map(str,map(int,a))))
