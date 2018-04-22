#include <iostream>
#include <string>
using namespace std;

int Str2Int(char*str)
{
	int number=0;
	while(*str!=0)
	{
		number = number*10+*str-'\0';
		++str;
	}
	return number;
}

int main()
{
	char str[]={'1','2','3','4'};
	//cin>>str;
	cout<<Str2Int(str)<<endl;
	return 0;
}

