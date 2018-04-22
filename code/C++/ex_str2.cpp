#include <iostream>
#include <string>

using namespace std;

int main()
{
	string s1,s2;
	cin>>s1>>s2;
	string::size_type len1,len2;
	len1 = s1.size();
	len2 = s2.size();
	if (len1==len2)
		cout<<"equal"<<endl;
	else if(len1>len2)
		cout<<"longer"<<endl;
	else
		cout<<"shorter"<<endl;
	return 0;
}
