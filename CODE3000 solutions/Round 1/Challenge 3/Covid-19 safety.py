import time
n=int(input())
l=[int(x) for x in input().split()]
t0=time.time()
flag=True
mx=n//3
if n%3!=0:
    mx+=1
#print(mx)
for i in range(n-1):
    if l[i]==1:
        if i==n-2 and l[i+1]==1:
            flag=False
            break
        else:
            if l[i+1]==1 or l[i+2]==1:
                flag=False
                break
if flag:
    print("Safe")
else:
    if l.count(1)<=mx:
        print("Unsafe and arrangement is possible")
    else:
        print("Unsafe and arrangement is not possible")
print(time.time()-t0)
print(l.count(0),l.count(1))
