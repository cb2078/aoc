d=[[+1,-1][c==')'] for c in open('01.txt').read().strip()]
r=R=0
for i,x in enumerate(d):
    r+=x
    if r==-1 and not R:
        R=i+1
print(r);print(R)
