#include <stdio.h>

typedef char C;
typedef int I;
typedef unsigned U;
typedef void V;

#define $(c,e...) if(c){e;}
#define F(n,e...) for(I i=0;i<(n);++i){e;}
#define P(c,e...) if((c)){return ({e;});}
#define R return
#define W(c,e...) while(c){e;}

#define oc(x) of("%c "(x))
#define od(x) of("%d ",(x))
#define of(x...) printf(x)
#define on() putchar('\n')
#define os(x) printf("%s ",(x))

#define xn x[-1]
#define xi x[i]
#define xj x[j]

#define yn y[-1]
#define yi y[i]
#define yj y[j]

#include <time.h>
#define tV(e...) ({struct timespec t0,t1;timespec_get(&t0,TIME_UTC);{e;};timespec_get(&t1, TIME_UTC);\
                  double d=difftime(t1.tv_nsec,t0.tv_nsec);if(d<0)d+=1e9;printf("%s: %lfms\n",#e,d/1e6);})
#define t(e...) ({struct timespec t0,t1;timespec_get(&t0,TIME_UTC);typeof(({e;})) x__=({e;});timespec_get(&t1, TIME_UTC);\
                  double d=difftime(t1.tv_nsec,t0.tv_nsec);if(d<0)d+=1e9;printf("%s: %lfms\n",#e,d/1e6);x__;})
