f=lambda x:len(set(x.replace('\n','')))
g=lambda x:len(set.intersection(*map(set,x.split('\n'))))
for h in f,g:print(sum(map(h,open('06.txt').read().strip().split('\n\n'))))

