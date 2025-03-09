import re
s=list(open('09.txt').read().strip())

def p(j):
    j+=1
    a=0
    while s[j].isnumeric():
        a*=10
        a+=int(s[j])
        j+=1
    assert s[j]=='x'
    j+=1
    b=0
    while s[j].isnumeric():
        b*=10
        b+=int(s[j])
        j+=1
    assert s[j]==')'
    return 1+j,a,b


i=0
while i<len(s):
    if s[i]!='(':
        i+=1
        continue
    j,a,b=p(i)
    s[i:j]=s[j:j+a]*(b-1)
    i+=a*b
print(len(s))

i=0
x=[1]*len(s)
while i<len(s):
    if s[i]!='(':
            i+=1
            continue
    j,a,b=p(i)
    for k in range(i,j):
        x[k]=0
    for k in range(j,j+a):
        x[k]*=b
    i=j
print(sum(x))
