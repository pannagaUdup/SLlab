li=[]
n=int(input("enter size"))
print("enter elements")
for i in range(n):
    li.append(int(input()))
print(li)
li.insert(int(input("enter pos")),int(input("enter element")))
print(li)
li.remove(int(input("enter element to delete")))
print(li)
max(li)
min(li)
try:
    pos=li.index(int(input("enter element to find")))
    print(pos)
except:
    print("element not found")
