import re
s=open('12.txt').read().strip()
print(sum(map(int,re.findall(r'-?\d+',s))))
f=lambda x:0 if type(x)==str else x if type(x)==int else sum(map(f,x)) if type(x)==list else 0 if 'red' in x.values() else sum(map(f,x.values()))
print(f(eval(s)))
