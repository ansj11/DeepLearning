#include <iostream>
using namespace std;

int fun(int n)
{
	int sum;
	if (n==0)
		sum = 0;
	else if (n==1)
		sum = 1;
	else
		sum = fun(n-1)+fun(n-2);
	return sum;
}

int main()
{
	int n,m;
	while(cin>>n)
	{
		for(int id = 0;id<n;id++)
		{ 
			cin>>m;
			if(m<1&m>40)
				break;
			
			cout<<fun(m)<<endl;
		}
	}
	return 0;
}
