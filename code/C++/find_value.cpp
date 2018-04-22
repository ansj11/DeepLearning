#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
	bool Find(int target,vector<int> array)
	{
		int height = sizeof(array)/sizeof(int);
		int width = sizeof(array[0])/sizeof(int);
		
		if (width==0)
			return false;
		
		int sum=0;
		for (int i=0;i<height;i++)
			for (int j=0;j<width;j++)
			{
				if (array[i][j]==target)
					sum += 1;
				else
					sum += 0;
			}
		if (sum==0)
			return false;
		else
			return true;
	}

};

int main()
{
	vector<int> a[][] = {{1,2,3},{4,5,6}};
	cout<<Solution::Find(2,a)<<endl;
	return 0;
}
