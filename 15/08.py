import re
s=open('08.txt').read().strip().split('\n')
def f(s):r=re.findall(r'(?:\\x[0-9a-fA-F]{2})|(?:\\.)',s);return 2+sum(map(len,r))-len(r)
g=lambda x:f('"%s"'%x.replace('\\','\\\\').replace('"','\\"'))
for h in [f,g]:print(sum(map(h,s)))
