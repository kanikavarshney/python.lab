import math
d=list(map(int,input("enter numbers").split(',')))
c=50
h=30
for i in d:
	q=math.sqrt(2*c*i/h)
	print(int(q),end=',')
