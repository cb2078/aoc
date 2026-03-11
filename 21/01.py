a=open('1.txt').read().split('\n')[:-1]
a=list(map(int,a))
b=sum(a[i]>a[i-1]for i in range(1,len(a)))
print(b)
a=[sum(a[i:i+3])for i in range(len(a)-2)]
b=sum(a[i]>a[i-1]for i in range(1,len(a)))
print(b)
