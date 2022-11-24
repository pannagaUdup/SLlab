# Write Python code to do the following:
# i. Create list with inputs from user
# ii. Determine minimum and maximum elements in the list
# iii. Insert new element into the list
# iv. Delete an element from the list
# v. Determine if an element is present in the list

#Initialize list
li=[]
n=int(input("enter no of elements"))
print("enter elements")
for i in range(n):
    li.append(int(input()))
while True:
    print("1.insert 2.minmax 3.delete 4.check-element 5.exit")
    x=int(input("enter your choice"))
    if x==1:
        a,b=(input("enter pos and element").split(" "))
        li.insert(int(a),int(b))
        print(li)
    elif x==2:
        print("max is ",max(li),"min is ",min(li))
    elif x==3:
        try:
            a=int(input("enter element to delete"))
            li.remove(a)
        except:
            print("element not found")
    elif x==4:
        try:
            a=int(input("enter element to find"))
            b=li.index(a)
            print("element is found in pos ",b)
        except:
            print("element is not found")
    else:
        break
