n,k=map(int,input().split())
l=[]
for _ in range(k):
    temp=[int(x) for x in input().split()]
    l.append(temp)
l.sort()
res=[0]*n
for i in l:
    if i[0]>i[1]:
        i[0],i[1]=i[1],i[0]
    res[i[0]-1]+=i[2]
    if i[1]<n:
        res[i[1]]-=i[2]
for i in range(1,n):
    res[i]+=res[i-1]
print(*res,sep=' ')
