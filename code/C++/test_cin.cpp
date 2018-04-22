#include <iostream>
using namespace std;

int main()
{
	int ITEMS = 10;
	int array[ITEMS];
	for(int i=0;i<ITEMS;i++)
	{
		cout << "Enter a aray:";
		while(!(cin>>array[i]))
		{
			cin.clear();
			cin.ignore(100,'\n');
			cout << "please enter a valid array:";
		}
	}
	for(int i=0;i<ITEMS;i++)
	{
		cout<<array[i]<<endl;
	}
}

