#include <iostream>
#include <string.h>

class People
{
	char name;
	int age;
	double sore;
};

struct Struct
{
	int a;
	char b;
	double c;
};

using namespace std;

int main()
{
	int age = 0;
	Struct st;
	st.a = 0;
	cout<<st.a<<endl;
	/*People ansj;
	ansj.age = age;*/
	return 0;
}
