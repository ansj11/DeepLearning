template <class T> 
class vector<T>
{
	

template <class T> 
void vector<T>::bubbleSort(vector<T>::iterator lo,vector<T>::iterator hi)
{while(!bubble(lo,hi--));}

template <class T> 
bool vector<T>::bubble(vector<T>::iterator lo,vector<T>::iterator hi)
{
	bool sorted = true;
	while(++lo<hi)
	{
		if(_elem[lo-1]>_elem[lo])
		{
			sorted = false;
			swap(_elem[lo-1],_elem[lo]);
		}
	}
	return sorted;
}
