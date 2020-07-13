n=int(input())
l=set(map(int,input().split()))
numbers = set(range(1,n+1))
print(list(numbers-l)[0])
