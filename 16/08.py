w,h=50,6
m=[['.']*w for _ in range(h)]
for s in open('08.txt').read().strip().split('\n'):
    match s.split():
        case ['rect', size]:
            x,y=map(int,size.split('x'))
            for i in range(y):
                for j in range(x):
                    m[i][j]='#'
        case ['rotate', 'row', row, 'by', n]:
            i=int(row.split('=')[-1])
            n=int(n)
            m[i]=m[i][-n:]+m[i][:-n]
        case ['rotate', 'column', col, 'by', n]:
            j=int(col.split('=')[-1])
            n=int(n)
            t=[m[(i-n)%h][j] for i in range(h)]
            for i in range(h):
                m[i][j]=t[i]
        case _:
            print(s)
            raise

print(sum(m[i][j]=='#' for i in range(h) for j in range(w)))
print('\n'.join(''.join(x) for x in m))
