#include <string.h>
#include <stdlib.h>
#include "a.h"

I w=0,h=0;V*rf(void){FILE*f=fopen("02.txt","rb");P(!f,0);C c;W((c=fgetc(f),'a'<=c&&c<='z'),++w)rewind(f);
    W(!feof(f),h+=fgetc(f)=='\n')rewind(f);C(*x)[w]=(C(*)[w])malloc(w*h);F(h,fscanf(f,"%s\r\n",xi))R x;}
V f(C*x,I*y,I*z){C d[26]={0};F(w,++d[xi-'a'])I yy=0,zz=0;F(26,yy|=2==d[i],zz|=3==d[i])*y+=yy,*z+=zz;}
I p1(V*b){C(*x)[w]=(C(*)[w])b;I y=0,z=0;F(h,f(x[i],&y,&z))R y*z;}
I m(C*x,C*y){I r=0;F(w,r+=xi==yi)R r+1==w;}I d(C*x,C*y){F(w,P(xi!=yi,i))R -1;}
V p2(V*b){C(*x)[w]=(C(*)[w])b;F(h,I j=1+i;W(j<h,P(m(x[i],x[j]),I k=d(x[i],x[j]);of("%.*s%.*s\n",k,xi,w-k-1,xi+k+1),(V)0)++j))}
int main(){V*b=rf();C(*M)[w]=(C(*)[w])b;R od(p1(M)),p2(M),0;}
