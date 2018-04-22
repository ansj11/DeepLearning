
#include <iostream>
#include <algorithm>

//正确算法是折半查找法,因为当取500000,500000时排序的运算量太大
using namespace std;

typedef long long int64;

int main()
{
	int64 n,m,k;
	//cin>>n>>m;
	while(cin>>m>>n>>k && m>=1 && n>=1 && k>=1 && k<=m*n)  
	{
		int64 num = n*m;
		int64 b[num];
		int64 i,j;
		for (i=0;i<n;i++)
		{
			for (j=0;j<m;j++)
				b[n*j+i] = (i+1)*(j+1);
		}
		sort(b,b+num);
		cout<<b[k-1]<<endl;
	}
	return 0;
}

