p=open('15.txt').read().strip().split('\n');h,w=len(p)-2,len(p[0].split()[0].strip())-2;m=[list(p[1+i][1:w+1]) for i in range(h)]
R=[(i,j) for i in range(h) for j in range(w)]
for i,j in R:m[i][j]=[m[i][j],200] if m[i][j] in 'GE' else m[i][j]
os=lambda u:'%c(%d)'%(u[0],u[1]);ou=lambda u:print(os(u))
om=lambda:print('\n'.join(''.join(m[i][j][0] for j in range(w))+'\t'+', '.join(os(m[i][j]) for j in range(w) if m[i][j][0] in 'GE') for i in range(h))+'\n')#;om()
from copy import deepcopy;m0=deepcopy(m)

def t(i,j):
    dirs=[(-1,0),(0,-1),(0,1),(1,0)]
    if m[i][j][0] not in 'GE':return
    i0,j0=i,j;u=m[i][j];m[i][j]='.';q=[(i,j,0)];p={(i,j):(i,j)};ts=set();d={};es=set()
    while q:
        i,j,n=q.pop(0);d[i,j]=n
        for di,dj in dirs:
            I,J=i+di,j+dj
            if I not in range(h) or J not in range(w):continue
            if m[I][J][0] in 'GE' and m[I][J][0]!=u[0]:ts.add((i,j));es.add((I,J))
            if (I,J) in p:continue
            if m[I][J][0]!='.':continue
            p[I,J]=i,j;q.append((I,J,n+1))
    if not ts:m[i0][j0]=u;return
    n=min(d[t] for t in ts);i,j=min(t for t in ts if d[t]==n) # by distance, then reading order
    while p[i,j]!=(i0,j0):i,j=p[i,j]
    m[i][j]=u # move
    if es:=es&{(i+di,j+dj) for di,dj in dirs}:
        I,J=min(es,key=lambda IJ:(m[IJ[0]][IJ[1]][1],IJ)) # enemy with lowest HP, then reading order
        m[I][J][1]-=3 if u[0]=='G' else a
        if m[I][J][1]<=0:m[I][J]='.'

# def t(i,j):
#     if m[i][j][0] not in 'GE':return
#     i0,j0=i,j;u=m[i][j];m[i][j]='.';q=[((i,j),)];v=set((i,j))
#     while q:
#         p=q.pop(0);i,j=p[-1];e=set()
#         for di,dj in [(-1,0),(0,-1),(0,1),(1,0)]:
#             I,J=i+di,j+dj
#             if I not in range(h) or J not in range(w) or (I,J) in v:continue
#             if m[I][J][0] in 'GE' and m[I][J][0]!=u[0]:e.add((I,J))
#             if m[I][J][0]!='.':continue
#             v.add((I,J));q.append(p+((I,J),))
#         if e:
#             if len(p)<=2: # attack
#                 I,J=min(e,key=lambda IJ:(m[IJ[0]][IJ[1]][1],IJ));m[I][J][1]-=3
#                 if m[I][J][1]<=0:m[I][J]='.'
#             k=min(len(p)-1,1);m[p[k][0]][p[k][1]]=u;return
#     m[i0][j0]=u;return

o=lambda:[(i,j) for i,j in R if m[i][j][0] in 'GE']
def r():
    for i,j in o():
        if any(all(m[i][j][0]!=c for i,j in R) for c in 'GE'):return False
        t(i,j)
    return True
def s(a_=3):
    global a;a=a_
    global m;m=deepcopy(m0)
    es=sum(m[i][j][0]=='E' for i,j in R)
    k=0#;print('Initially:');om()
    while r():k+=1#;print('After',k,'rounds');om()
    # print('Finally:');om()
    # print(k,x:=sum(m[i][j][1] for i,j in R if m[i][j][0] in 'GE'),k*x) # 188232<ans<194028, 190960???
    return (k*sum(m[i][j][1] for i,j in R if m[i][j][0] in 'GE'),
            sum(m[i][j][0]=='E' for i,j in R)==es)
print(s(3)[0]) # p1
from itertools import count
for k in count():
    out,b=s(k)
    if b:print(out);break
