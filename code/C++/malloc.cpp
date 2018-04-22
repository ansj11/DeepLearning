#include <iostream>
#include <cmalloc>
#include <string>
using namespace std;

char *DuplicateString(char* s)
{
	char*t;
	unsigned int n,i;
	if (!s){cout<<"Error\n";}
	n = strlen(s);
	t = (char*)malloc(n+1);
	for (i=0;i<n;i++)
		t[i] = s[i];
		t[n] = '\0';
	return t;
}

