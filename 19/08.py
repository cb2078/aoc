x=*map(int,list(open('08.txt').read().strip())),
n=25*6
y=max((x[i:i+n] for i in range(0,len(x),n)),key=lambda x:-x.count(0))
print(y.count(1)*y.count(2))
print('\n'.join(''.join(' #'[next(x[25*i+j+k] for k in range(0,len(x),n) if k==len(x)-n or x[25*i+j+k]<2)]
                        for j in range(25)) for i in range(6)))
