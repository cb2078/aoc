a=[*map(int,s:=open('16.txt').read().strip())]
b=0,1,0,-1
n=len(a)

for _ in range(100):
  a=[abs(sum(a[j]*b[(j+1)//(i+1)&3]for j in range(n)))%10 for i in range(n)]
print(''.join(map(str,a[:8])))

a=[a[i%n] for i in range(int(s[:7]),n*10000)]
for _ in range(100):
  s=0
  for i in range(len(a))[::-1]:
    a[i]=s=(s+a[i])%10
print(''.join(map(str,a[:8])))
