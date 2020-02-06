a = int(input("enter the number"))
sum = 0
for i in range(1,a-1):
	if(a%i==0):
		sum=sum+i
if(a==sum):
	print("prime number")
else:
	print("not prime")
	


  
