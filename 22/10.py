f=[x.split() for x in open('10.txt').read().rstrip().split('\n')]
from itertools import accumulate, islice
r=list(accumulate((0 if x == ['noop'] else int(x[1]) for x in f), initial = 1))
c=[[2,1][x == ['noop']] for x in f] + [1]
r=[x for i,x in enumerate(r) for _ in range(c[i])]
print(sum((i+1)*x for i,x in enumerate(r) if 0==(i+21)%40)) # 1
w=40;h=6
print('\n'.join(islice(accumulate(range(len(r)),
                                  lambda s,i:s[:i%w]+' #'[r[i]-1<=i%w<=r[i]+1]+s[(i%w)+1:],
                                  initial=' '*w),
                       w-1, None, w))) # 2
