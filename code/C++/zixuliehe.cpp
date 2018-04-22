#include<iostream>
#include<vector>
using namespace std;

struct operation{
	int opt;
	int first;
	int end;
}; //结构体数据的创建

//改变一个位置的权值
int change(int* a,int num,int value){
	a[num - 1] = value;
	return 0;
}

//求连续子序列的和
int add(int *a,int first,int end){
	int kk=0;
	for (int i = first - 1; i < end;i++){
		kk += a[i];
	}
	return kk;
}

//求连续格子的最大值
int maxVal(int *a, int first, int end){
	int kk = a[first - 1];
	for (int i = first; i < end; i++){
		kk = (a[i]>kk?a[i]:kk);
	}
	return kk;
}

int main(){
	int n, m;
	while (cin>>n>>m){
		int *data=new int[n];
		for (int i = 0; i < n; i++){
			cin >> data[i];
		}
		vector<operation>opts;
		for (int i = 0; i < m;i++){
			operation option;
			cin >> option.opt >> option.first >> option.end;
			opts.push_back(option);
		}
		for (int i = 0; i < m; i++){
			if (opts[i].opt==1){
				change(data, opts[i].first, opts[i].end);
			}
			else if (opts[i].opt == 2){
				
				cout << add(data, opts[i].first, opts[i].end) << endl;
			}
			else if (opts[i].opt == 3){
				cout << maxVal(data, opts[i].first, opts[i].end) << endl;
			}
		}
	}
	return 0;
}

	
