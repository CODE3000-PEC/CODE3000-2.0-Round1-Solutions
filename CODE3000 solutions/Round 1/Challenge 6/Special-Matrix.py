n = int(input())
mat = [ [ 0 for i in range(n)]for j in range(n)]
    
    
for i in range(1,n+1):
    for j in range(1,n+1):
        m = max(i,j)
        mat[i-1][j-1] = str(((i-j)*(-1)**m+m*m-m+1))
    
for i in mat:
    
    print(*i,sep="\t")
