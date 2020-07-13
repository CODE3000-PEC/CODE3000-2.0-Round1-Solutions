t = int(input())
for _ in range(t):
    s = input()
    s1 = ''
    i = 0
    s1 = '('*int(s[0]) + s[0]
    open_count = int(s[0])
    close_count = 0
    for i in range(1,len(s)):
        if(s[i-1] == s[i]):
            s1 += s[i]
        elif(s[i-1] > s[i]):
            n = int(s[i-1]) - int(s[i])
            s1 += ')'*n
            close_count += n
            s1 += s[i]
        elif(s[i-1]<s[i]):
            n = int(s[i]) - int(s[i-1])
            s1 += '('*n
            open_count += n
            s1 += s[i]
    if(open_count>close_count):
        n = open_count - close_count
        s1 += ')'*n
    print(s1)
