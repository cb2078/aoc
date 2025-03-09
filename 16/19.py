from collections import deque as d
n=int(open('19.txt').read().strip())

x=d(range(1,n+1))
while len(x)>1:
    x.rotate(-1)
    x.popleft()
print(x[0])

x=d(range(1,n+1))
x.rotate(n//2*-1)
while len(x)>1:
    x.popleft()
    x.rotate(len(x)%2-1)
print(x[0])
