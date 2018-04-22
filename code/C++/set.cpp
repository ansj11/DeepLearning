#include <iostream>
#include <set>
using namespace std;

int main()
{
	int a[6] = {1,2,2,3,5,5};
	int	*b = set(a);
	
	for (int i=0;i<sizeof(b)/sizeof(int);i++)
		cout<<a[i]<<endl;
	return 0;
}
