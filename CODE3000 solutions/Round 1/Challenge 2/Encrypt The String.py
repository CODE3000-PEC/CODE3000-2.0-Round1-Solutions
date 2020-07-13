s = list(input())
alpha = list('abcdefghijklmnopqrstuvwxyz')
l = ['' for i in range(len(s))]
for i in range(len(s)):

    value = ((ord(s[i])-97) + ord(s[i])%26)%26

    l[i] = alpha[value]
        
print(''.join(l))
