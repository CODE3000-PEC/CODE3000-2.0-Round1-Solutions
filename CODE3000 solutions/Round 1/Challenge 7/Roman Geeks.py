import random
def int_to_roman(num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
def returnNum(key):
    dic = {'C':12,'D':13,'I':18,'L':21,'M':22,'V':31,'X':33}
    return dic[key]
    
def largest_base(R):
    temp = []
    for i in range(len(R)):
        temp.append(R[i])
    R = temp
    temp = sorted(R)
    base = (returnNum(temp[len(temp)-1]))
    return base,R
if __name__ =='__main__':

    N=int(input())
   
    n=0
    while(N<4000):
        R = int_to_roman(N)
        base , R = largest_base(R)
        star = base+1
        j = len(R)-1
        n = 0
        for i in range(0,len(R)):
            star1 = returnNum(R[i]) * (star ** j)
            n += star1
            j -= 1
        N = n
    print(n)
