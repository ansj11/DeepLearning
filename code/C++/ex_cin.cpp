#include <iostream>

using namespace std;
int main()

{
	int amount = 0,value;
	while(cin>>value)
	{if (value<0)
		++amount;}
	cout<<amount<<endl;
	string line;
	while(getline(cin,line))
		cout<<line<<endl;
	return 0;
}

