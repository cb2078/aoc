W,G=[x.split('\n') for x in open('24.txt').read().strip().split('\n\n')]
W=dict((lambda x,y:(x,int(y)))(*x.split(': ')) for x in W);W0=W
G=dict((lambda x:(x[-1],x[:-1]))(x.replace(' -> ', ' ').split()) for x in G)

g=lambda x:sum(W[w]<<int(w[1:]) for w in W if w[0]==x)
o=lambda x:print(f'{x} {g(x):064b} {g(x)}')

import operator as op
def f(w):
    g={'AND':op.and_,'OR':op.or_,'XOR':op.xor}
    if w not in W:x,o,y=G[w];W[w]=g[o](f(x),f(y))
    return W[w]
while k:=G.keys()-W.keys():
    for w in k:f(w);break
print(g('z'))#;quit()

# For part 2 print out the tree of operations for each wire and then check if
# it is a full adder; if it isn't then swap the wrong wire with the correct one
# and make note of the swap. Repeat this until the all the gates form a full 44
# bit adder. It is easier to do this by changing the input file each time than
# to do it programatically.

def h(z,n=0):
    if n==3 or z[0] in 'xy':return z
    d={'AND':'&','OR':'|','XOR':'^'}
    x,o,y=G[z];hx,hy=h(x,n+1),h(y,n+1);h0,h1=[f(hx,hy) for f in [min,max]]
    return '(%s%s%s)'%(h1,d[o],h0)
def H(z):
    if z[0] in 'xy':return 1
    x,y=G[z][::2]
    return H(x)+H(y)
print(*[x+' %3d'%H(x)+' '+h(x)[1:-1] for x in sorted(G.keys())],sep='\n')
