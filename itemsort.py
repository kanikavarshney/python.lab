l=[]
while 1:
	item = input("enter the item")
	l.append(item)
	n = input("do u want to continue y\\n")
	if n.lower()=='n':
	   break
l.sort(reverse=True,key=len)
print(l)
