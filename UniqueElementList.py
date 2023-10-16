n=int(input("Enter n number of elements in list "))
list1=[]
list2=[]
for i in range(0,n):
    num=int(input("Enter num element in list1 "))
    list1.append(num)
    
flag=0    
for i in range(0,n):
    flag=0
    for j in range(0,len(list2)):
        if(list1[i]==list2[j]):
            flag=1
            
    if flag==0:
        list2.append(list1[i])
        
for i in range(0,len(list2)):
    print(list2[i])
        
    
