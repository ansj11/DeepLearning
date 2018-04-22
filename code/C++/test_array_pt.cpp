#include <iostream>
using namespace std;

template <class type>
void printArray(type a)
{
	int items = 3;
	for(int i=0;i<items;i++)
	cout<<a[i]<<" ";
}

int main()
{
	const unsigned short ITEMS = 3;
	int Array[ITEMS] = {98,-486,301589};
	char charArray[ITEMS] = {'A','B','C'};
	double douArray[ITEMS] = {4.1423,2.793,7.321};
	
	int *pt1 = Array;
	char *pt2 = charArray;
	double *pt3 = douArray;

	printArray(Array);
	for(int i=0;i<ITEMS;i++)
	{
		cout<<*pt1<<" at "<<(unsigned long)(pt1)<<endl;
		pt1++;
	}
}
