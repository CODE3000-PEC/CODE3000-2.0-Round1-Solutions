N=int(input())
k=int(input())
k1=k
incre = 1
spaces=N-1
for i in range(N):
    for j in range(5*spaces):
        print(" ",end="")
    for j in range(incre):
        print("%.5d"%k,end="")
        k+=k1
    print()
    incre+=2
    spaces-=1
