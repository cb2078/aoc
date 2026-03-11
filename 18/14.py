n=824501;l=[3,7];p=[0,1]
while len(l)<n+10:
    l+=list(map(int,str(l[p[0]]+l[p[1]])))
    for i in range(2):p[i]+=l[p[i]]+1;p[i]%=len(l)
print(''.join(map(str,l[n:n+10])))

# r='824501';s='37';p=[0,1]
# while r not in s[-10:]:
#     xs=[ord(s[p[i]])-ord('0') for i in range(2)];s+=str(sum(xs))
#     for i in range(2):p[i]+=1+xs[i];p[i]%=len(s)
# print(s.index(r))

r=list('824501');l=[0xc8]*30000000;l[:2]='37';ln=2;p=[0,1];rn=len(r);b=True
while b:
    xs=[ord(l[p[i]])-ord('0') for i in range(2)]
    for d in str(sum(xs)):
        l[ln]=d;ln+=1
        if l[ln-rn:ln]==r:print(ln-rn);b=False
    for i in range(2):p[i]+=1+xs[i];p[i]%=ln
