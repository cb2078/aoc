from collections import defaultdict
g={}
v=defaultdict(list)
o=defaultdict(list)

for s in open('10.txt').read().strip().split('\n'):
    match s.split():
        case ['value', x, 'goes', 'to', 'bot', b]:
            v['b'+b].append(int(x))
        case ['bot', b, 'gives', 'low', 'to', tl, xl, 'and', 'high', 'to', th, xh]:
            g['b'+b]=(tl[0]+xl,th[0]+xh)
        case _:
            print(s)
            raise

s=[b for b in v if len(v[b])==2]
while s:
    b=s.pop(0)
    for bb,f in zip(g[b],[min,max]):
        v[bb].append(f(v[b]))
        if len(v[bb])==2:
            s.append(bb)

[print(b[1:]) for b in v if 17 in v[b] and 61 in v[b]]
print(v['o0'][0]*v['o1'][0]*v['o2'][0])
