n,m = map(int,input().split())
l=[]
for i in range(n):
    temp = list(map(int,input().split()))
    l.extend(temp[1:temp[0]+1])
l.sort(reverse=True)
for i in range(len(l)-1,-1,-1):
    if l[i]>0:
        break
l=l[:i+1]
s=sum(l[:m])
[print(0) if s<0 else print(s)]

