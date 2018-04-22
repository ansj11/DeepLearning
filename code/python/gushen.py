


def Getprice(n):
	i = 0       #Decrease days
	j = 2     	#Increase days after i th decrease
	k = n 
	while(j<k):
		i+=2
		k-=j
		j = j+1
	return n-i

while(True):	
	n = input()
	print Getprice(n)
