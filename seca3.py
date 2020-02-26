l=list(map(int,input("enter numbers").split(",")))
for i in l:
	a=1
	for j in range(1,i+1):
		a=a*j
	print(a,end=',')
		
		
