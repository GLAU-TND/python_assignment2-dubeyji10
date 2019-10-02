l = eval(input("enter a list: "))

def decreasinglist(a):
    num = 0
    for i in range(1,len(a)):
        if a[i]<a[i-1]:
            num +=1
    return num <=1

p =decreasinglist(l)
print(p)