k=open('04.txt').read().strip()
from hashlib import md5
from itertools import count
p=1
for i in count(1):
    h=md5((k+str(i)).encode()).hexdigest()
    if p==1 and h.startswith('0'*5):print(i);p+=1
    if p==2 and h.startswith('0'*6):print(i);break
