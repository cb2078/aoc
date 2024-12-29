from collections import defaultdict
import re
d=defaultdict(int)
m=0
for r,op,x,R,cmp,y in re.findall(r'(\w+) (inc|dec) (-?\d+) if (\w+) (\S+) (-?\d+)',open('8.txt').read()):
    exec(f"if d['{R}'] {cmp} {y}:\n    d['{r}'] {'+-'[op=='dec']}= {x}")
    m=max(m,max(d.values()))
print(max(d.values()))
print(m)
