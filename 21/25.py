a=[*map(list,open('25.txt').read().strip().split('\n'))]
for t in range(1,9**9):
  b=a
  for c,(x,y) in zip('>v',((0,1),(1,0))):
    a=[[c if a[i][j]=='.' and a[i-x][j-y]==c else
        '.' if a[i][j]==c and a[(i+x)%len(a)][(j+y)%len(a[0])]=='.' else
        a[i][j] for j in range(len(a[0]))] for i in range(len(a))]
  # print(t,'\n'.join(''.join(x) for x in b),sep='\n',end='\n\n')
  if b==a:
    print(t)
    break
