#include <iostream>
using namespace std;

void PrintArray(int *p,int n)
{
	int i;
	for (i=0;i<n;i++)
		cout<<*(p+i)<<" ";
	
	cout<<endl;
}

void ReverseInt(int *p,int n)
{
	int i,t;
	for (i=0;i<n;i++)
		 t = *(p+i);
		 *(p+i) = *(p+n-i-1);
		 *(p+n-i-1) = t;
}

int main()
{
	int a[8] = {1,2,3,4,8,7,6,5};
	int *p = &a[0];
	//p = &a[0];
	PrintArray(p,8);
	ReverseInt(p,8);
	PrintArray(p,8);
	return 0;
}
