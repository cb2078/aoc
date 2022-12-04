p=open('03.txt').read().strip().split("\n")

import string

priority={c:i+1 for i,c in enumerate(string.ascii_lowercase)}|\
    {c:i+27 for i,c in enumerate(string.ascii_uppercase)}

def score(r):
    l=len(r)//2
    return ''.join(set(r[l:])&set(r[:l]))

print(sum(priority[score(r)]for r in p)) # 1
print(sum(priority[''.join(set.intersection(*map(set,p[i:i+3])))]for i in range(0,len(p),3))) # 2
