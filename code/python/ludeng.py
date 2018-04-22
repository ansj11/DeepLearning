
while(1):
	s = raw_input().split()
	
	n = int(s[0])
	l = int(s[1])
	
	a = [int(i) for i in raw_input().split()]
	
	d = []
	
	b = sorted(a)
	
	d.append(b[0])
	
	for i in range(1,len(a)):
		r = (b[i]-b[i-1])/2.0
		d.append(r)
	
	d.append(l-b[-1])
	
	print ('%.2f' % max(d))
