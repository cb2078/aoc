k=set('byr iyr eyr hgt hcl ecl pid'.split())
p=[dict(x.split(':') for x in s.split('\n')) for s in open('04.txt').read().strip().replace(' ','\n').split('\n\n')]
p=[d for d in p if k<=d.keys()]
print(len(p))

a=0
for d in p:
  b=1
  for k,v in d.items():
    match k:
      case 'byr':
        b&=1920<=int(v)<=2002
      case 'iyr':
        b&=2010<=int(v)<=2020
      case 'eyr':
        b&=2020<=int(v)<=2030
      case 'hgt':
        if 'cm' in v:
          x=int(v.replace('cm',''))
          b&=150<=x<=193
        elif 'in' in v:
          x=int(v.replace('in',''))
          b&=59<=x<=76
        else:
          b=0
      case 'hcl':
        b&=v[0]=='#' and all(x in '1234567890abcdef' for x in v[1:]) and len(v)==7
      case 'ecl':
        b&=v in 'amb blu brn gry grn hzl oth'.split()
      case 'pid':
        b&=len(v)==9 and v.isdigit()
      case 'cid':
        pass
      case _:
        print(k)
        raise
  a+=b
print(a)
