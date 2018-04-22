#include <iostream>
using namespace std;

int main()
{
	int a = 31280;
	float b = 32.78;
	char c = 'D';
	string s = "asdkl";
	int e = -12;
	cout<<"Address is: "<<(unsigned long)&a<<endl;
	cout<<(unsigned long)&b<<endl;
	cout<<(unsigned long)&c<<endl;
	cout<<(unsigned long)&s<<endl;
	cout<<(unsigned long)&e<<endl;
	return 0;	
}
