for i,f,o in zip(range(9),['addr','mulr','banr','borr','setr','gtrr','eqrr'],[*'+*&| >','==']):
    exec(s:=f'def {f}(a,b,c):x[c]='+('x[a]' if i==4 else f'x[a]{o}x[b]'))
    for x,y,z in ['rib'] if i<4 else ['ria'] if i==4 else [('rr','ri','b'),('rr','ir','a')]:
        exec(s.replace(x+'(',y+'(').replace('x[%s]'%z,z))
i,*p=open('21.txt').read().strip().split('\n');i=int(i.split()[-1])
p=[eval('lambda:%s(%s)'%((w:=p[j].split())[0],','.join(w[1:]))) for j in range(len(p))]

x=[0]*6;v=set()
while x[i]<len(p):
    if x[i]==28:
        if not v:print(x[3])
        if x[3] in v:print(y);break
        v.add(y:=x[3])
    p[x[i]]();x[i]+=1

'''
     #ip 5
 0 | seti 123 0 3           | x3=123
                              .l1
 1 | bani 3 456 3           | x3=x3&456
 2 | eqri 3 72 3            | x3=x3==72
 3 | addr 3 5 5             | goto 5 if x3
 4 | seti 0 0 5             | goto 1
                              .l5
 5 | seti 0 9 3             | x3=0
                              .l6
 6 | bori 3 65536 1         | x1=x3|65536
 7 | seti 14906355 8 3      | x3=14906355
                              .l8
 8 | bani 1 255 4           | x4=x1&255
 9 | addr 3 4 3             | x3=x3+x4
10 | bani 3 16777215 3      | x3=x3&16777215
11 | muli 3 65899 3         | x3=x3*65899
12 | bani 3 16777215 3      | x3=x3&16777215
13 | gtir 256 1 4           | x4=256>x1
14 | addr 4 5 5             | goto 16 if x4
15 | addi 5 1 5             | goto 17
                              .l16
16 | seti 27 8 5            | goto 28
                              .l17
17 | seti 0 4 4             | x4=0
                              .l18
18 | addi 4 1 2             | x2=x4+1
19 | muli 2 256 2           | x2=x2*256
20 | gtrr 2 1 2             | x2=x2>x1
21 | addr 2 5 5             | got 23 if x2
22 | addi 5 1 5             | goto 24
                              .l23
23 | seti 25 1 5            | goto 26
                              .l24
24 | addi 4 1 4             | x4=x4+1
25 | seti 17 2 5            | goto 18
                              .l26
26 | setr 4 9 1             | x1=x4
27 | seti 7 0 5             | goto 8
                              .l28
28 | eqrr 3 0 4             | x4=x3==x0
29 | addr 4 5 5             | exit if x4
30 | seti 5 3 5             | goto 6
'''
