from itertools import permutations
import math
def is_prime(n): 
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n > 2 and n % 2 == 0: 
        return False
  
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2): 
        if n % i == 0: 
            return False
    return True 
l = list(input())
Possible=[]
perm=[]
flag=0
for i in range(1,len(l)+1):
    Possible.extend(list(permutations(l,i)))
for i in Possible:
    perm.append(int("".join(i)))
perm.sort()
for i in perm[::-1]:
    if is_prime(i):
        print(i)
        break
else:
    print("Not Found")
