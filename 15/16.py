import re
s=open('16.txt').read()
s=re.sub(r'([A-Za-z]+)',r'"\1"',s)
s=re.sub(r'\S+ (\d+:) (.*)\n',r'\1 {\2}, ',s)
s='{%s}'%s[:-2]
D=eval(s)
d={'children':3,'cats':7,'samoyeds':2,'pomeranians':3,'akitas':0,'vizslas':0,'goldfish':5,'trees':3,'cars':2,'perfumes':1}
f=lambda k,x,y:x>y if k in ['cats','trees'] else x<y if k in ['pomeranians','goldfish'] else x==y # f(k,D[i][k],d[k])
g=lambda k,x,y:x==y
for h in [g,f]:print(next(i for i in D if all(h(k,D[i][k],d[k]) for k in D[i])))
