import time
n=int(input())
t=time.time()
l1=[int(x) for x in input().split()]
l2=[int(x) for x in input().split()]
res=0
l1=sorted(l1,reverse=True)
l2=sorted(l2,reverse=True)
c=0
for i in range(n):
    for j in range(c,n):
        if l1[i]>l2[j]:
            #print(l1[i],l2[j])
            c=j+1
            res+=1
            break
print(res)
print(time.time()-t)
