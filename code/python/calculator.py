#/usr/bin/python
#-*- coding: utf-8 -*-


while(1):
	n = raw_input()
	if n!=""and 1<n<=1000000:
		n = int(n)
		k = n
		a = []
		while (k>1):
			for i in range(1,k):
				if k%i==0 and i!=1:
					k = k/i
					a.append(i)
					break
				elif k%i==0 and i==1:
					break
				else:
					continue
			
	print sorted(a)
