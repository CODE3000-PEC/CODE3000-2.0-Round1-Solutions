

    
def f(n,r):
    l = []
    l1 = []
    r = r
    cond = n*(n+1)//2
    num = 1
    if cond%2 == 0:
        flag1 = 0
        flag2 = 1
        
        if n%2 != 0:
            if n == 3:
                l = [1,2]
                l1 = [3]
            else:
                l = [1,2,4]
                l1 = [3]
                for i in range(5,n+1,2):
                    if flag1 == 0:
                        l1.append(i)
                        if i+1<n+1:
                            l1.append(i+1)
                        flag1 = 1
                        flag2 = 0
                    elif flag2 == 0:
                        l.append(i)
                        if i+1<n+1:
                            l.append(i+1)
                        flag2 =1
                        flag1 = 0

                    
        else:
            flag1 = 0
            flag2 = 1
            rev = n
            for i in range(n//2):
                if flag1 == 0:
                    l.append(i+1)
                    l.append(rev)
                    rev-=1
                    flag1 = 1
                    flag2 = 0
                elif flag2 == 0:
                    l1.append(i+1)
                    l1.append(rev)
                    rev-=1
                    flag2 = 1
                    flag1 = 0
            

        
        
        print('YES')
       
        
        print(*l,sep=' ')
        
        print(*l1,sep=' ')
        
    else:
        print('NO')
        
n = int(input())
f(n,n)
    
    
