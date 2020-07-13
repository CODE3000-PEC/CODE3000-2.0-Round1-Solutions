import time
n=int(input())
t=time.time()
res=1
sum=1
if n==1:
    print(res)
else:
    for i in range(2,n+1):
        res=sum*i*2
        sum+=res
    print(res)
    print(len(str(res)))
print(time.time()-t)       
