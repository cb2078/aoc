from collections import defaultdict
from itertools import takewhile,combinations

P=defaultdict(int)
for i,x in enumerate(open('25.txt').read().strip().split(',')):
  P[i]=int(x)

def f():
  E=lambda j:p[i+j] if (x:=p[i]//10**(j+1)%10)==0 else i+j if x==1 else p[i+j]+b if x==2 else ...
  e=lambda j:p[E(j)]

  def a(j,x):
    nonlocal i
    k=E(j)
    assert k>=0
    p[k]=x
    i+=j+1

  p=P.copy()
  b=0
  i=0
  while True:
    match p[i]%100:
      case 1:
        a(3,e(1)+e(2))
      case 2:
        a(3,e(1)*e(2))
      case 3:
        a(1,(yield 'I'))
      case 4:
        yield e(1)
        i+=2
      case 5:
        i=e(2) if e(1) else i+3
      case 6:
        i=e(2) if not e(1) else i+3
      case 7:
        a(3,e(1)<e(2))
      case 8:
        a(3,e(1)==e(2))
      case 9:
        b+=e(1)
        i+=2
      case 99:
        break
      case _:
        print(i,p[i])
        raise

O=lambda:print(end=''.join(map(chr,takewhile(lambda x:x!='I',p))))

def g(x):
  for y in x+'\n':
    p.send(ord(y))
  print(x)
  O()

h='''\
east
west
west
take hypercube
west
take space law space brochure
west
north
take shell
west
take mug
west
south
take festive hat
north
east
south
east
east
east
east
north
west
north
take whirled peas
west
west
take astronaut ice cream
south
inv'''

i=['hypercube',
   'space law space brochure',
   'festive hat',
   'shell',
   'astronaut ice cream',
   'mug',
   'whirled peas']

for x in i:
  h+='\ndrop '+x
h+='\ninv'

p=f();O()
for x in h.split('\n'):
  g(x)

try:
  for x in (y for x in range(len(i)) for y in combinations(i,x+1)):
    for y in x:
      g('take '+y)
    g('inv')
    g('south')
    for y in x:
      g('drop '+y)
except StopIteration:
  pass

'''
...................................
..................................
..................................
..................................
..................................
.......hf< st< a..................
.......v.......^..................
.......cp......sc< w..............
.......v...........^..............
.......@.*<hd< hb> c..............
..................................
...........k< e < gw..............
..................^...............
..............n < sb<*st..........
..................................
..................................
..................................
..................................
..................................
..................................

don't take the photons
don't take the giant electromagnet
don't take infiniate loop
don't take the escape pod

a: whirled peas
hf: ice ceam
hd: hypercube
s: brochure
gf: shell
e: mug
k: festive hat (actually south of egineering)
'''
