#include "a.h"
#include <stdlib.h>
#include <string.h>

/*C*z;
C*p1(I n){C x[2],*s=malloc(16);U a,y[2]={0,1},zn=0;z[zn++]='3',z[zn++]='7';
 W(zn<n+10,a=0;F(2,a+=xi=z[yi]-'0')sprintf(s,"%d",a);F((I)strlen(s),z[zn++]=s[i])F(2,yi+=1+xi,yi%=zn))R snprintf(s,11,"%s",&z[n]),s;}
U p2(C*r){U y[2]={0,1},a,rn=strlen(r),zn=0;C x[2],s[16];z[zn++]='3',z[zn++]='7';
 W(20,a=0;F(2,a+=xi=z[yi]-'0')sprintf(s,"%d",a);F((I)strlen(s),z[zn++]=s[i];P(zn>=rn&&!strncmp(&z[zn-rn],r,rn),zn-rn))F(2,yi+=1+xi,yi%=zn))R 0;}
int main(){R z=t(malloc(1e9)),os(t(p1(824501))),on(),od(t(p2("824501"))),0;}
// int main(){I rs[]={9,5,18,2018,824501};z=malloc(1e9);F(5,os(p1(rs[i])),on())R 0;}
// int main(){C*rs[]={"51589","01245","92510","59414","824501"};z=malloc(1e9);F(5,od(p2(rs[i])),on());R 0;}*/
C *z,*s="824501";U n=824501;int main(){U p1=1,p2=2,y[2]={0,1},a,sn=strlen(s),zn=0;C x[2],b[16];z=malloc(1e9),z[zn++]='3',z[zn++]='7';
 W(p1||p2,a=0;F(2,a+=xi=z[yi]-'0')sprintf(b,"%d",a);F((I)strlen(b),z[zn++]=b[i];$(p2&&zn>=sn&&!strncmp(&z[zn-sn],s,sn),p2=0,os("p2"),od(zn-sn),on()))F(2,yi+=1+xi,yi%=zn)
  $(p1&&zn>n+10,p1=0,of("p1 %.*s\n",10,&z[n])))R 0;}
