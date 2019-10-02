l = eval(input("enter a list of numbers enclosed in [] : "))
#print(l,type(l))
a = int(input("enter a number : "))

def prob2(list1,num):
    start = 0
    p=len(list1)
    sum=0
    list2=[]
    for i in range(0,p):
        while(sum>num):
            #print(sum,"reducing")
            sum-=int(list1[start])
            start+=1
            #print(sum,"reduced")
        if sum==num:
            #print(sum,"is found b/w indexes ",start," and ",i-1)
            list2=list1[start:i]
            #print(list2)
            return list2
        if i<p:
            sum+=int(list1[i])
list3 = prob2(l,a)
if type(list3)==None:
    print("no such subarray ")
else:
    print(list3)