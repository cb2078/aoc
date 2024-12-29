s=int(open('17.txt').read().strip())
from collections import deque
b=deque([0])
for n in range(1,2018):
    b.rotate(-s)
    b.append(n)
print(b[0])

i=0
for n in range(1,50000001):
    i=(i+s+1)%n
    if i==0:
        x=n
print(x)
