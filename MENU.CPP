#include<stdio.h>
#include<conio.h>
int key;
int binary(int [],int ,int );
int linear(int [],int ,int );
main()
{
clrscr();
 int n,i,a[10],pos,ch;
do
{
	printf("-------Menu--------\n1.Binary Search\n2.Linear Search\n3.Exit");
 printf("\nEnter your choice ");
 scanf("%d",&ch);
 switch(ch)
 {
 case 1 :
  printf("\n Enter how many elements: ");
  scanf("%d",&n);
  printf("\n Enter elements of array\n");
  for(i=0;i<n;i++)
  {
  scanf("%d",&a[i]);
  }
  printf("\n enter the elements to be searched");
  scanf("%d",&key);
  pos=binary(a,n,key);
  if(pos==-1)
  printf("\n element not found");
  else
  printf("\n element found at position %d",pos+1);
  break;
 case 2 :
  printf("\n Enter how many elements: ");
  scanf("%d",&n);
  printf("\n Enter elements of array\n");
  for(i=0;i<n;i++)
  {
  scanf("%d",&a[i]);
  }
  printf("\n enter the elements to be searched");
  scanf("%d",&key);
  pos=linear(a,n,key);
  if(pos==-1)
  printf("\n element not found");
  else
  printf("\n element found at position %d",pos+1);
  break;

default:printf("\n Invalid coice");
 break;
 }
}
while(ch!=3);
}
int binary(int a[],int x,int search)
{
 int beg=0,last=x-1;
 int mid;


 if(beg>last)
 {
  return(-1);
 }

 mid=(beg+last)/2;
 while(beg<=last)
 {
  if(search==a[mid])
  {
  return(mid);
  }
  if(search<a[mid])
  {
  last=mid-1;
  }
  else
  {
  beg=mid+1;
  }
  mid=(beg+last)/2;
 }
}


int linear(int a[],int x, int search)
{
 int i;
 for(i=0;i<x;i++)
 {
 if(a[i]==search)
 return(i);
 }
 return(-1);
}