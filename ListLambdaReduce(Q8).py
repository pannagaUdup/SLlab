from functools import reduce
list=[1,2,3,4,5,6]
listc=[(lambda x:3*x)(x)for x in list]
print(listc)
print(reduce(lambda x,y:x+y,list))