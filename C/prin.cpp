#include <stdio.h>
#include <conio.h>
void fibonnaci_series(int num,int n1,int n2,int n3){
	for (int i=0;i<num;i++){
		n3=n2+n1;
		printf(n3);
		n1=n2;
		n2=n3;
	}
}
int main(){
	int n,n1=0,n2=1,n3,n;
	printf(n1);
	printf(n2);
	printf("Enter a number :");
	scanf("%d",&n);
	fibonnaci_series(n,n1,n2,n3);
}


