#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<int> a;
	cout<<sizeof(a)<<endl;
	cout<<sizeof(a)/sizeof(int)<<endl;
	cout<<sizeof(a[0])<<endl;
	return 0;
}

