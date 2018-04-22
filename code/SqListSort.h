#ifndef SQLIST_H
	#define SQLIST_H
	#include "SqList.h"
#endif

#define KEYNUM 3
#define RADIX 10

template <typename ElemType>
calss SqListSort:public SqList<ElemType>
{
public:
	//zheban charu
	void binaryInsertSort();
	
	void bubleSort();
	
	int getIndex();
	
	void heapSort();
	
	void insertSort();
	
	void mergeSort();
	
	void quickSort();
	
	void radixSort();
	
	void ShellSort();
	
	void selectSort();
	
	void staticLinkListSort();
	
private:
	
	void heapSortAdjust_aux(int s,int t);
	
	void mergeSort_aux(int s,int t);
	
	void mergeSortOne_aux(int low,int,high);
	
	void quickSort_aux(int low,int high);
	
	int quickSortPartition_aux(int low,int high);
	
	void radixSortCollect_aux(int front[],int end[],int time);
	
	void radixSortDistribute_aux(int i,int front[],int end[]);
	
	void ShellSort_aux(int dk);
	
public:
	
	SqListSort();
	
	~SqListSort();
	
	SqListSort(const SqListSort & s);

protected:
	
	int *index;
};

