from hashlib import md5

s=open('14.txt').read().strip()

for r in 1,2017:
    x={}
    y={}
    i=0
    n=0
    while n<64:
        h=s+'%d'%i
        for _ in range(r):
            h=md5(h.encode()).hexdigest()
        for j in range(len(h)-2):
            if h[j]==h[j+1] and h[j]==h[j+2]:
                x[i]=h[j]
                break
        for j in range(len(h)-5):
            if all(h[j]==h[j+k] for k in range(1,5)):
                y[i]=h[j]
                break
        k=i-1000
        for j in range(max(0,k+1),i+1):
            if k in x and j in y and x[k]==y[j]:
                n+=1
                break
        i+=1
    print(k)
