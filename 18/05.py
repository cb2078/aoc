s=open('05.txt').read().strip()
def f(s):
    l=list(s);b=True
    while b:
        b=False
        for i in range(len(l)-1)[::-1]:
            if b := l[i]!=l[i+1] and l[i+1].lower()==l[i].lower():
                del l[i:i+2]
                if i+1>=len(l):
                    break
    return len(l)
print(f(s)) # p1 # <33782
def r(s,c):return f(s.replace(c.lower(),'').replace(c.upper(),''))
import string
print(min(r(s,c) for c in string.ascii_lowercase)) # p2
