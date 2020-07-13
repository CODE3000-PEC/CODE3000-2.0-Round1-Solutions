'''C = cucumber slices and O = Onion slices
   Let x = Number of large sandwiches and y = Number of small sandwiches
   So, x + y = O and 4x + 2y = C
      --> x = C/2 - O and y = 2O - C/2
   The following 3 conditions have to be satisfied in order to make sure that no slices are left:
     1. C has to be even i.e.,C%2==0
     2. x>=0 i.e.,C/2-O>=0 --> C>=2*O
     3. y>=0 i.e.,2*O - C/2>=0 --> 4*O>=C
'''
C,O=map(int,input().split())
if C%2==0 and C>=2*O and 4*O>=C:
    print(C//2-O,2*O-C//2)
else:
    print("Not Possible")
