k=int(open('20.txt').read().strip());n=1000000
for p in 0,1:
    h=[0]*n
    for i in range(1,n):
        for j in range(i,min(i+i*50,n) if p else n,i):h[j]+=(10+p)*i
        if h[i]>k:
            print(i)
            break
