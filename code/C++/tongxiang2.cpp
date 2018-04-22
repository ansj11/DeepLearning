#include <iostream>//并查集简单应用
using namespace std;
#define N 1001
int n,m;
int pa[N]; 
void makeset(int n)
{
	for(int i=1;i<=n;++i)
		pa[i]=i;
}
int findset(int x)
{
      if(x!=pa[x]) 
        pa[x]= findset(pa[x]);
    return  pa[x];
}
void unionset(int x,int y)
{
  //x = findset(x);
  //y = findset(y);
  if(x == y)
		return ;
	pa[x] = y;
}
int main()
{
    int n,m,a,b,i;
    while(cin>>n>>m)
    {
		if(n==0&&m==0)
			break;
		makeset(n);
    for(int i=0;i<m;++i)
        {
			cin>>a>>b;
			a=findset(a);
			b=findset(b);
			unionset(a,b);
		}
		int cnt=0;
		int result=findset(1);
        for(int i=2;i<=n;++i)
		{
           if(findset(i)==result)
			   ++cnt;
		}
           cout << cnt<< endl; 
        }
    return 0;
}
