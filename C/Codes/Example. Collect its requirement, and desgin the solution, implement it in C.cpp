//To make a system that takes the marks from the students and generate their  grades and show them.
#include <stdio.h>
#include <conio.h>
int main()
{
	int marks;
	char grade;
	printf("\nEnter the marks of the student.");
	scanf("%d",&marks);
	if (marks<0 and marks>100)
	{
		printf("Not possible.");
	}
	if (marks>75)
	   grade ='0';
	else if(marks<75 && marks>60)
	   grade ='A';
	else if(marks<60 && marks>50)
	   grade ='B';
	else if(marks<50 && marks>40)
	   grade ='C';
	else
	   grade ='0';
	printf("\nGrade = %c",grade);          
}

