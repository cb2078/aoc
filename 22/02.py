p=open('02.txt').read().strip().split('\n')
p=[[{'A':0,'B':1,'C':2,'X':0,'Y':1,'Z':2}[x] for x in row.split()] for row in p]
wins=[1,2,0]
score = lambda x, y: 1 + y + (3 if x == y else 6 if wins[x] == y else 0)
print(sum(score(row[0], row[1]) for row in p))
draws=list(range(3))
losses=[wins.index(i) for i in range(3)]
# print(losses,draws,wins,sep='\n')
score = lambda x, y: [losses[x], draws[x] + 3, wins[x] + 6][y] + 1
print(sum(score(row[0], row[1]) for row in p))
