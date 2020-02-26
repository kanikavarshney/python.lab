st=input("enter string")
subst=input("enter substring")
k=-1
c=0
for i in range(len(st)):
	k=st.find(subst,k+1)
	c=c+1
print(c)
