class CCompute
{
protected:
	int i, j;
public:
	CCompute(int a,int b)
	{
		i=a;
		j=b;
	}
	
	~CCompute(){}
	
	int sum();
	int minus();
	
};
