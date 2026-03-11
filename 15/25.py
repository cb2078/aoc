import re;t=[*map(int,re.findall(r'\d+',open('25.txt').read().strip()))]
i=j=0
n=20151125
while [i+1,j+1]!=t:
    n=n*252533%33554393
    i,j=i-1,j+1
    if i<0:
        i,j=j,0
print(n)
