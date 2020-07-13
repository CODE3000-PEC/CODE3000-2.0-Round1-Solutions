n=int(input())
l=[int(x) for x in input().split()]
dp=[0]*n
dp[0]=l[0]
dp[1]=max(l[0],l[1])
for i in range(2,n):
    dp[i]=max(dp[i-2]+l[i],dp[i-1])
print(dp[n-1])
