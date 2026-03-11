pi=open('2.txt').read().split('\n')[:-1]
pi=[x.split() for x in pi]

h=d=a=0

for i in pi:
    v=int(i[1])
    match i[0]:
        case 'down':
            a+=v
        case 'up':
            a-=v
        case 'forward':
            h+=v
            d+=a*v
print(h*d)

# 5144850 (low)
