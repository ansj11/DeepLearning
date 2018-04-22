#include <stdio.h>
#include "Compute.h"

int main(void)
{
	CCompute computeObj(3,8);
	printf("3和8求和:%d\n",computeObj.sum());
	printf("3和8求差:%d\n",computeObj.minus());
	return 0;
}
