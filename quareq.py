a = int(input("enter the value of a"))
b = int(input("enter the value of b"))
c = int(input("enter the value of c"))
d = (b**2-4*a*c)
if d>=0:
        print("roots are exists")
        x = (-b+(d**1/2))/2*a
        y = (-b-(d**1/2))/2*a
        print("roots = ",x,y)
else:
       print("roots are not exists")



