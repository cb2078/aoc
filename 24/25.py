p=[x.split('\n') for x in open('25.txt').read().strip().split('\n\n')];n,w,h=len(p),len(p[0][0]),len(p[0])
k=[i for i in range(n) if p[i][0]=='#'*w];l=[i for i in range(n) if i not in k]#;print(k,l,sep='\n')
p=[[sum(k[i][j]=='#' for i in range(h)) for j in range(w)] for k in p]
print(sum(all(p[i][k]+p[j][k]<=h for k in range(w)) for i in k for j in l))
