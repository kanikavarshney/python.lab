l=list(map(int,input("enter the number").split(',')))
l1=[]
for i in range(1,len(l)):
	if i not in l:
		l1.append(i)
print(l1)
