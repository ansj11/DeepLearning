
void GenerateInt(int *p,unsigned int n)
{
	unsigned int i;
	Randomize();
	for(i=0;i<n;i++)
	{
		*p++ = random(low,up);
	}
}

void ReverseInt(int *p,int n)
{
	int i;
	for (i=0;i<n;i++)
		int t = p+i;
		p+i = p+n-i-1;
		p+n-i-1 = p+i;
}
