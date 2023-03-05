#include <iostream>

using namespace std;

int i = 5;
int j = 7;
int *p = &i;
int *q = &j;
int &r = i;
int &s = j;

int main()
{
  void print();
  cout << "\t\t";
  cout << "i"
       << "\t";
  cout << "j"
       << "\t";
  cout << "p"
       << "\t\t";
  cout << "*p"
       << "\t";
  cout << "q"
       << "\t\t";
  cout << "*q"
       << "\t";
  cout << "r"
       << "\t";
  cout << "&r"
       << "\t\t";
  cout << "s"
       << "\t";
  cout << "&s" << endl;
  cout << "Start\t\t";

  print();
  i = *p * *q;
  cout << "i = *p * *q;"
       << "\t";
  print();
  s = r;
  cout << "s = r"
       << "\t\t";

  print();
  *p = 12;
  cout << "*p = 12;"
       << "\t";

  print();
  q = p;
  cout << "q = p;"
       << "\t\t";

  print();
  r = s / 5;
  cout << "r = s / 5"
       << "\t";

  print();
  j = *p + *q;
  cout << "j = *p + *q;"
       << "\t";

  print();
  return 0;
}

void print()
{
  cout << i << "\t";
  cout << j << "\t";
  cout << p << "\t";
  cout << *p << "\t";
  cout << q << "\t";
  cout << *q << "\t";
  cout << r << "\t";
  cout << &r << "\t";
  cout << s << "\t";
  cout << &s << endl;
}