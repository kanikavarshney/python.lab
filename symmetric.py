l1=[1,3,4,2]
l2=[1,4,9,5]
l3=[x1 for x1 in l1 if x1 not in l2 ]
l4=[x2 for x2 in l2 if x2 not in l1]
print(l3+l4)

