#include <iostream>
using namespace std;

#include "random.h"
#include "arrmanip.h"

#define NUM 8

int main()
{
	int a[NUM];
	GenerateInt(a,NUM);
	cout<<"Array is: \n"
	PrintInt(a,NUM);
	ReverseInteger(a,NUM);
	cout<<"reversed:\n";
	PrintInt(a,NUM);
	return 0;
}
