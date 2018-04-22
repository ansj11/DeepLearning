#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

int main()
{
	int n,m,k;
	//cin>>n>>m;
	while(cin>>m>>n>>k && m>=1 && n>=1 && k>=1 && k<=m*n)  
	{
		int num = n*m;
		int b[num];
		for (int i=0;i<n;i++)
		{
			for (int j=0;j<m;j++)
				b[n*j+i] = (i+1)*(j+1);
		}
		
		for(int i=0;i<num;i++)
			cout<<b[i]<<" ";
		cout<<endl;
		
		sort(b,b+num);
		
		for(int i=0;i<num;i++)
			cout<<b[i]<<" ";
		cout<<endl;
		cout<<"k-th number is: "<<b[k-1]<<endl;
	}
	return 0;
}
		
