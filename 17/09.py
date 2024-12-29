s=open('9.txt').read().strip()
n=1
i=0
j=False
x=0
y=0
while i<len(s):
    if j:
        match s[i]:
            case '>':
                j=False
            case '!':
                i+=1
            case _:
                y+=1
    else:
        match s[i]:
            case '{' :
                n+=1
            case '}':
                n-=1
                x+=n
            case ',':
                pass
            case '<':
                j=True
            case '_':
                raise
    i+=1

print(x)
print(y)
