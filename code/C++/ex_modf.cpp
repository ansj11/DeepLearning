#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	double x;
	double *y;
	cin >>x;
	cout<< modf(x,y)<<endl;
	double z;
	cin>>z;
	cout<< fmod(x,z)<<endl;
	return 0;
}
