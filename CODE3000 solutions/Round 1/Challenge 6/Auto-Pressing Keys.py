s=input()
res=[]
ind=0
num=1
end=False
for i in range(len(s)):
    if s[i]=="*" and len(res)>0:
        res.pop()
    elif s[i]=="<":
        end=False
        ind=0
    elif s[i]==">":
        end=True
    elif s[i]=="#":
        if num==0:
            num=1
        else:
            num=0
    elif s[i].isdigit():
        if num:
            res.insert(ind,s[i])
            ind+=1
    else:
        if end:
            res.append(s[i])
        else:
            res.insert(ind,s[i])
            ind+=1
    print(res)
print(''.join(res))
    
        
        
