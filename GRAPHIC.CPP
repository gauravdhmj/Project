#include<graphics.h>
#include<conio.h>

void main()
{
int gd=DETECT , gm;
initgraph(&gd , &gm ,"C:\\TURBOC3\\BGI");
  setbkcolor(4);
circle(300,250,200);
  setcolor(1);
rectangle(23,67,89,79);
  setcolor(2);
arc(759,438,348,776,76);
  setcolor(3);
ellipse(64,34,3,30,56);
  setcolor(4);
circle(200,150,30);
  setcolor(5);
circle(400,150,30);
  setcolor(6);
arc(300,230,220,320,150);
  setcolor(7);
line(280,250,310,250);
  setcolor(8);
line(280,250,300,200);
getch();
closegraph();
}
