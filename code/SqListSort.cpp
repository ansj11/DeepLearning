
template <typename T>

void SqListSort<T>::binaryInsertSort()
{
	int low;
	int mid;
	int high;
	int k=-1;
	T key;
	
	for (int i=1;i<n;++i)
	{
		key = elm[i];
		low = 0;
		high = i-1;
		
		while(low<=high)
		{
			mid = (low+high)/2;
			if (key<elem[mid])
				high = mid-1;
			else
				low = mid+1;
		}
		
		for (int j=i-1;j>=high+1;--j)
			elem[j+1] = elem[j];
		elem[high+1]=key;
	}
}

template <typename T> 
void SqListSort<T>::bubbleSort()
{
	bool flag = true;
	T t;
	
	for (int i=1;i<n&&flag;++i)
	{
		for (int j=0;j<n-i;++j)
		{
			if (elem[j+1]<elem[j])
			{
				flag = true;
				t = elem[j+1];
				elem[j+1] = elem[j];
				elem[j] = t;
			}
		}
	}
}

template <typename T>
int SqListSort<T>::getIndex(int i)
{
	if (i<1||i>n) return -1;
		return index[i-1];
}

template <typename T>
void SqListSort<T>::heapSort()
{
	int i,j=1;
	T t;
	
	for (i=n/2-1;i>-1;--i)
		heapSortAdjust_aux(i,n-1);
	
	for (i=n-1;i>1;--i)
	{
		t= elem[i];
		elem[i] = elem[0];
		elem[0] = t;
		
		heapSortAdjust_aux(0,i-1);
	}
}
