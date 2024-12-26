import re
a,b,c,*p=map(int,re.findall(r'\d+',open('17.txt').read().strip()));n=len(p)#;print(a,b,c,p)

def f(a,b,c):
    i=0;o=[]
    C=lambda x:x if 0<=x<=3 else [a,b,c][x-4]
    while i<n-1:
        x=p[i+1]
        match p[i]:
            case 0:a=a//(2**C(x))
            case 1:b=b^x
            case 2:b=C(x)%8
            case 3:i=x-2 if a else i
            case 4:b=b^c
            case 5:o.append(C(x)%8)
            case 6:b=a//(2**C(x))
            case 7:c=a//(2**C(x))
        i+=2
    return o

print(','.join(map(str,f(a,b,c))))

s=[0]
for i in range(n):
    for _ in range(len(s)):
        x=s.pop(0)
        for j in range(8):
            a=8*x+j
            if f(a,b,c)[0]==p[n-1-i]:
                s.append(a)
    print(*s,p[n-i-1:])
print(min(s))
