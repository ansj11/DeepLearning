#include <iostream>
using namespace std;

int main()
{
    int year,month,date;
    cout<<"Enter year, month, date: ";
    cin>>year>>month>>date;
    int a[12];
    for (int i=0;i<12;i++)
    {
        if (i==0||i==2||i==4||i==6||i==7||i==9||i==11)
            a[i] = 31;
        else if (i==1)
        	{
            if ((year%4==0 && year%100!=0)||(year%400==0))
                a[i] = 29;
            else
                a[i] = 28;
            end}
        	else
            	a[i] = 30;
        	end
        end
    }
    int sum = 0;
    for (int i = 0;i<month-1;i++)
        sum += a[i];
    sum += date;
    cout<<"The date is "<<sum<<"th day"<<endl;
    return 0;
}
