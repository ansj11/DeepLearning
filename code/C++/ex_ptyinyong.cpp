#include <iostream>
using namespace std;
int main()
{
	int a = 1024,b=2048;
	int *c = &a,*d = &b;
	c = d;
	cout<<*c<<endl;
	int &p = a,&q = b;
	p=q;
	cout<<&p<<endl;
	return 0;
}
