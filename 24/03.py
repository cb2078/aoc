import re
p=open('03.txt').read().replace('\n','')
r=r'mul\(\d{1,3},\d{1,3}\)'
m=re.findall(r,p)#;print(*m,sep='\n')
f=lambda x:(lambda x,y:x*y)(*map(int,re.findall(r'\d+',x)))
print(sum(map(f,m))) # p1
b=1;x=0
for i in range(len(p)):
    s=p[i:]
    if s.startswith("do()"):b=1
    if s.startswith("don't()"):b=0
    if not b:continue
    if M:=re.match(r,s):x+=f(M[0])
print(x) # p2
