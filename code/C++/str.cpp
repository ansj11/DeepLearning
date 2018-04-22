#include <iostream>
using namespace std;

int Find(char c,char *s)
{
	if (!s)
	{
		cout<<"Error!"<<endl;
	}
	char *t;
	for (t=s;t!='\0';t++)
	{
		if (*t==c)
			return t-s;
	}
}

int main()
{
	char s[9] = "absdks !";
	char *p = &s[0];
	cout<<Find('o',p)<<endl;
	string q = "abcdef";
	cout<<Find('o',s)<<endl;
	return 0;
}
