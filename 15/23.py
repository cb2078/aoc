for a in 0,1:
    r=dict(zip('ab',[a,0]));i=0
    for f,o,x in zip(['inc','hlf','tpl'],['+','//','*'],'123'):
        exec(f'def {f}(x):r[x]{o}={x}')
    def jmp(o):
        global i;
        i+=o-1
    for f,o in zip(['jie','jio'],['r[x]%2==0','r[x]==1']):
        exec(f'def {f}(x,o):global i;i+={o} and o-1')
    p=open('23.txt').read().strip().split('\n')
    while i<len(p):
        # print('%2d'%i,p[i],r)
        w=p[i].replace(',','').split()
        w[1]="'%s'"%w[1] if w[1] in 'ab' else w[1]
        eval(s:=f'{w[0]}({', '.join(w[1:])})')
        i+=1
    print(r['b'])
