s=input()
L=list(s.split())
#sorting the list in lexicographical order
ls=sorted(L)
#sorting the list according to the length of the strings
new=sorted(ls,key=len)
#considering the length of the largest string
max_len=len(new[-1])
for i in new:
    print(i.center(max_len,' '))
