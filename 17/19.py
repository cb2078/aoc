m=open('19.txt').read().rstrip().split('\n')
n=len(m)
for i in range(n):
    m[i]+=' '*(n-len(m[i]))

i=0
j=m[i].index('|')
di,dj=1,0
r=''
s=0
while True:
    match m[i][j]:
        case '|':
            pass
        case '+':
            di,dj=dj,di
            if i+di not in range(n) or j+dj not in range(n) or m[i+di][j+dj]==' ':
                di,dj=-di,-dj
        case '-':
            pass
        case _ if m[i][j].isalpha():
            r+=m[i][j]
        case ' ':
            break
        case _:
            raise
    i,j=i+di,j+dj
    s+=1
print(r)
print(s)
