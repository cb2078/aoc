m=open('06.txt').read().strip().split('\n')
for f in max,min:print(''.join(f(set(r),key=lambda x:r.count(x)) for r in zip(*m)))
