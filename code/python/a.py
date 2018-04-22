import numpy as np

str = raw_input()
str = str.split('-')
year = int(str[0])
month = int(str[1])
date  = int(str[2])

if((year%4==0 and year%100!=0) or (year%400==0)):
    a = np.array([31,29,31,30,31,30,31,31,30,31,30,31])
else:
    a = np.array([31,28,31,30,31,30,31,31,30,31,30,31])

s = 0
for i in range(month-1):
    s += a[i]

s += date

print "%d-%d-%d is the No.%d day of %d" % (year,month,date,s,year)