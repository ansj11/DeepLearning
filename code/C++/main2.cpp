#include "Compute2.h"
#include "stdio.h"

int main(void)
{
	CCompute2 compute2Obj(6,5);
	printf("6和5的乘积:%d\n",compute2Obj.mul());
	return 0;
}
