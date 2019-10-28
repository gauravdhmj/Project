#include<graphics.h>
#include<conio.h>

void main()
{
int gd=DETECT , gm;
initgraph(&gd , &gm ,"C:\\TURBOC3\\BGI");
circle(300,250,200);
circle(200,150,30);
circle(400,150,30);
arc(300,230,220,320,150);
line(280,250,310,250);
line(280,250,300,200);
getch();
closegraph();
}