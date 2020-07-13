def fun(n):
    num = list(map(str,range(1,n+1)))
    alpha = list(map(chr,range(97,97+n)))

    s = ''.join(num) + ''.join(alpha[::-1])

    length = len(''.join(num))
    length1 = len(''.join(alpha[::-1]))

    
    l = ['' for i in range(n)]
    l[-1] = s
    for i in range(n-2,-1,-1):
        num.pop()
        alpha.pop()
        l[i] = ''.join(num).ljust(length) + ''.join(alpha[::-1]).rjust(length1) 

    print(*l,sep='\n')
    #return l

fun(int(input()))

