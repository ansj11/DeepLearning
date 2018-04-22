#include <iostream>
#include <vector>
using namespace std;

int Add(int *data,int first,int end)
{
	int sum = 0;
	for(int i=first;i<=end;i++)
	{
		sum += data[i];
	}
	return sum;
}

int main()
{
	int n;
	while(cin>>n)
	{
		int *data = new int[n];
		for(int i =0;i<n;i++)
			cin>>data[i];
		
		int a[n][n];
		for(int i=0;i<n;i++)
			for(int j=i;j<n;j++)
			{
				a[i][j] = Add(data,i,j);
			}
		
		int maxVal = 0;
		int begin,end;
		for(int i=0;i<n;i++)
			for(int j=i;j<n;j++)
			{
				if (a[i][j]>maxVal)
				{	maxVal = a[i][j];
					begin = i;
					end = j;
				}
			}
		cout<<"begin: "<<begin+1<<" end: "<<end+1<<" max sum: "<<maxVal<<endl;
	}
	return 0;
}
