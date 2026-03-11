for i,f,o in zip(range(9),['addr','mulr','banr','borr','setr','gtrr','eqrr'],[*'+*&| >','==']):
    exec(s:=f'def {f}(a,b,c):x[c]='+('x[a]' if i==4 else f'x[a]{o}x[b]'))
    for x,y,z in ['rib'] if i<4 else ['ria'] if i==4 else [('rr','ri','b'),('rr','ir','a')]:
        exec(s.replace(x,y).replace('x[%s]'%z,z))
i,*p=open('19.txt').read().strip().split('\n');i=int(i.split()[-1]);
p=[eval('lambda:%s(%s)'%((w:=p[j].split())[0],','.join(w[1:]))) for j in range(len(p))]
def l1():x[0]=sum(i for i in range(1,x[5]+1) if x[5]%i==0);x[3]=16**2
for j in 0,1:
    x=[j]+[0]*5;p[1]=l1 if j else p[1]
    while x[i]<len(p):p[x[i]]();x[i]+=1
    print(x[0])

# def l1():
#     x[2]=1
#     while True:
#         x[4]=1
#         while True:
#             if x[2]*x[4]==x[5]:
#                 x[0]+=x[2]
#             x[4]+=1
#             if x[4]>x[5]:
#                 x[2]+=1
#                 if x[2]>x[5]:
#                     x[3]=16*16
#                     return
#                 else:
#                     break

'''
goto l17            addi 3 16 3     0
.l1
x2=1                seti 1 5 2      1
.l2
x4=1                seti 1 5 4      2
x1=x2*x4            mulr 2 4 1      3
x1=x1==x5           eqrr 1 5 1      4
goto l7 if x1       addr 1 3 3      5
goto l8             addi 3 1 3      6
.l7
x0=x2+x0            addr 2 0 0      7
.l8
x4=x4+1             addi 4 1 4      8
x1=x4>x5            gtrr 4 5 1      9
goto l12 if x1      addr 3 1 3      10
goto l3             seti 2 7 3      11
.l12
x2=x2+1             addi 2 1 2      12
x1=x2>x5            gtrr 2 5 1      13
goto l16 if x1      addr 1 3 3      14
goto l2             seti 1 4 3      15
.l16
goto l197 (exit)    mulr 3 3 3      16
.l17
x5=x5+2             addi 5 2 5      17
x5=x5*x5            mulr 5 5 5      18
x5=19*x5            mulr 3 5 5      19
x5=x5*11            muli 5 11 5     20
x1=x1+3             addi 1 3 1      21
x1=x1*22            mulr 1 3 1      22
x1=x1+12            addi 1 12 1     23
x5=x5+x1            addr 5 1 5      24
goto x3+x0+1        addr 3 0 3      25
goto l1             seti 0 5 3      26
x1=27               setr 3 4 1      27
x1=x1*28            mulr 1 3 1      28
x1=29+x1            addr 3 1 1      29
x1=30*x1            mulr 3 1 1      30
x1=x1*14            muli 1 14 1     31
x1=x1*32            mulr 1 3 1      32
x5=x5+x1            addr 5 1 5      33
x0=0                seti 0 9 0      34
goto 1              seti 0 4 3      35
