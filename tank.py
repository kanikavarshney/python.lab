r = 5
h= 10
f= 10
vtank=3.14*r*r*h
t = int(input(enter the time"))
vwtr=f*t
if vwtr>vtank:
       print('overflow)
       print('volume',vwtr-vtank)
elif vwtr == vtank:
      print('tank full')
else:
      print('underflow condition')
      ht = vwtr/(3.14*r**2)
      hr = h - ht
      print('filled height',ht.'remaining height')


