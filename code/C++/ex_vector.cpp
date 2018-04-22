#include <iostream>
#include <vector>

using namespace std;

int main(void)

{
	vector<string> vec;
	vector<string>::const_iterator i;
	vec.push_back("dog");
	vec.push_back("bird");
	vec.push_back("ansj win");
	for (i=vec.begin();i!=vec.end();++i)
		cout<<*i<<endl;
	
	return 0;
}
