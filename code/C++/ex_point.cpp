#include <iostream>
using namespace std;

int main()
{
	int i=42;
	void *p = &i;
	cout<<p<<endl;
	int *lp = &i;
	cout<<lp<<endl;
	cout<<*lp<<endl;
	string s = "hello world";
	string *sp = &s;
	*sp = "goodbye";
	cout<<sp<<" "<<s<<endl;
	string s2 = "ansj";
	sp = &s2;
	cout<<sp<<" "<<*sp<<endl;
	return 0;
}
