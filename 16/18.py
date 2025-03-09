for n in 40,400000:
    s='.'+open('18.txt').read().strip()+'.'
    x=s.count('.')-2
    for _ in range(n-1):
        s='.'+''.join('.^'[s[i-1:i+2] in ('^^.','.^^','^..','..^')] for i in range(1,len(s)-1))+'.'
        x+=s.count('.')-2
    print(x)
