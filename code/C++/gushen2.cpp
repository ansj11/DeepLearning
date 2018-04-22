#include <iostream>
using namespace std;

int GetPrice(int n)
{
	int i=0;
	while(2+i+(i+3)*i/2<n)
		i++;
	
	return n-2*i;
}

int main()
{
	int n;
	while(cin>>n)
		cout<<GetPrice(n)<<endl;
	
	return 0;
}
