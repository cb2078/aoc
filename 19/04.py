i,j=map(int,open('04.txt').read().strip().split('-'))
for p in [1,2]:
    print(sum(any(s.count(c)>=2 if p==1 else s.count(c)==2 for c in s) and
              all(s[i]<=s[i+1] for i in range(5)) for s in map(str,range(i,j+1))))
