#include <stdio.h>
int main(){
	int a,b,c;
	scanf("%d%d",&a,&b);

	while ((c=a%b)!=0){	//Õ·×ªÏà³ý·¨ 
		a=b;
		b=c;
	}
	
	if (b==1) printf("yes");
	else printf("no");
}

