from hashlib import md5
i=0
p=''
P='-'*8
d=open('05.txt').read().strip()
while len(p)<8 or '-' in P:
    h=md5((d+str(i)).encode()).hexdigest()
    if h.startswith('0'*5):
        if len(p)<8:
            p+=h[5]
        j=int(h[5],16)
        if j<8 and P[j]=='-':
            P=P[:j]+h[6]+P[j+1:]
    i+=1
print(p,P,sep='\n')
