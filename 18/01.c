#include <stdlib.h>
#include <string.h>
#include "a.h"

// V ob(U x){F(32,printf("%llu",(x>>(31-i))&1))os("\n");}
// I c(I x){static I n=0,a[200'000];F(n,P(a[i]==x,1))R a[n++]=x,0;}
I c(I x){x+=200;static U bs[100000]={0};U i=x/32,b=1<<(x%32);R bs[i]&b?1:(bs[i]|=b,0);}
I p1(I*x){I r=0;F(xn,r+=xi)R r;}
I p2(I*x){I r=0,i=0;c(r);W(1,r+=xi;P(c(r),r)i=i==xn-1?0:i+1)}
int main(){FILE *f=fopen("01.txt","rb");I*x=(I*)malloc(1000*sizeof(I));*x++=0;W(!feof(f),fscanf(f,"%d\r\n",&x[xn++]))
    od(t(p1(x))),od(t(p2(x)));R 0;}
