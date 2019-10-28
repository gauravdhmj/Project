#include<iostream.h>
#include<conio.h>
#include<stdlib.h>
int genhash() ;
struct Node
{
  int Data ;
  int prevhash ;
  int currhash ;
  Node *Next ;
};
class Block
{
  public:
  Node *head,*tail ;
  Block()
  {
    head= NULL ;
    tail=NULL ;
  }
  void NewBlock() ;
  void DisChain() ;
  ~Block() ;
};
void Block::NewBlock()
{
  Node *Temp ;
  Temp= new Node ;
  cout<<"Enter Data:" ;
  cin>>Temp->Data ;
  Temp->Next = NULL ;
  if(head== NULL)
  {
    head = Temp ;
    tail = Temp ;
    Temp->prevhash = genhash() ;
    Temp->currhash = genhash() ;
  }
  else
  {
    Temp->currhash= genhash() ;
    Temp->prevhash=tail->currhash ;
    tail->Next=Temp ;
    tail=tail->Next ;
  }
}
void Block::DisChain()
{
  Node *Temp ;
  Temp= head ;
  while(Temp!=NULL)
  {
    cout<<"|"<<Temp->Data<<":"<<Temp->prevhash<<":"<<Temp->currhash<<"|->" ;
    Temp=Temp->Next ;
  }
}
Block::~Block()
{
  while(head !=NULL)
  {
    Node *Temp=head ;
    head=head->Next ;
    delete Temp ;
  }
}
int genhash()
{
  return rand() ;
}
void changenode( Block B ,int no)
 {
   Node *temp ;
   temp = B.head ;
   while ( --no )
     {
       temp = temp ->Next;
     }
   cout << " Changing the data : " ;
   cin >> temp->Data;
   temp->currhash = genhash();
   if ( temp -> currhash != temp -> Next -> prevhash )
     {
	temp -> Next = NULL ;
     }
   temp = B.head ;
   while(temp!=NULL)
  {
    cout<<"|"<<temp->Data<<":"<<temp->prevhash<<":"<<temp->currhash<<"|->" ;
    temp=temp->Next ;
  }
 }
void main()
{
  clrscr() ;
  Block B ;
  int i,j ;
  cout<<"BlockChain"<<endl ;
  cout<<"1.New Block 2.Display Chain 3.corrupting"<<endl ;
  do
  {
    cin>>i ;
    switch(i)
    {
      case 1:B.NewBlock() ; break ;
      case 2:B.DisChain() ; break ;
      case 3:cout << " chnaging node : " ; cin >> j ; changenode(B,j); break ;
      default: cout<<"Wrong Input"<<endl ;
    }
  }while(i!=4) ;
}
