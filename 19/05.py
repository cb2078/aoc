P=[*map(int,open('05.txt').read().strip().split(','))]
e=lambda j:p[p[i+j]] if 0==p[i]//10**(j+1)%10 else p[i+j]
def a(j,x):global i;p[p[i+j]]=x;i+=j+1

for x in 1,5:
    p=P.copy()
    i=0
    while True:
        match z:=p[i]%100:
            case 1:
                a(3,e(1)+e(2))
            case 2:
                a(3,e(1)*e(2))
            case 3:
                a(1,x)
            case 4:
                if y:=e(1):
                    print(y)
                i+=2
            case 5:
                i=e(2) if e(1) else i+3
            case 6:
                i=e(2) if not e(1) else i+3
            case 7:
                a(3,e(1)<e(2))
            case 8:
                a(3,e(1)==e(2))
            case 99:
                break
            case _:
                print(i,p,z)
                raise

