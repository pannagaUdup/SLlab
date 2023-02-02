class Reverse:
    string=""
    def __init__(self,string):
        self.string=" ".join(reversed(string.split()))
print("enter 3 strings")
objarr=[]
cv=[0,0,0]
dict={}
for i in range(3):
    objarr.append(Reverse(input()))
    for j in range(len(objarr[i].string)):
        if objarr[i].string[j].lower() in ['a','e','i','o','u']:
            cv[i]+=1
    dict.update({objarr[i].string:cv[i]})
print(*sorted(dict.items(),key=lambda x:x[1],reverse=True),sep='\n')   
