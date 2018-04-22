											
while 1:
    n=raw_input()
    if n!="":
        n=int(n)
        a=[int(i) for i in raw_input().split()]
        b=sorted(a)
        c=[a[i] for i in range(n) if a[i]!=b[i]]
        start=a.index(c[0])
        end=a.index(c[-1])
        if a[:start]+list(reversed(a[start:end+1]))+a[end+1:]==b:
            print "yes"
        else:
            print "no"
    else:
        break

										
