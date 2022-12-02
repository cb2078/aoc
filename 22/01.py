p=open('01.txt').read().strip().split('\n\n')
p=[sum(map(int,x.split('\n')))for x in p]
print(max(p)) # 1
print(sum(sorted(p)[-3:])) # 2
