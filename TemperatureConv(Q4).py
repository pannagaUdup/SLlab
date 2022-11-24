# Write a temperature converter python program, which is menu driven. Each such
# conversion logic should be defined in separate functions. The program should call the
# respective function based on the user‘s requirement. The program should run as long as the
# user wishes so. Provide an option to view the conversions stored as list of tuples with attributes
# - from unit value, to unit value sorted by the user‘s choice (from-value or to-value).

#inital list to store conversion
history=[]
#converion logic for temprature
def ktoc(a):
    return a-273.15
def ctok(a):
    return a+273.15
def ctof(a):
    return  9.0/5.0 * a + 32
def ftoc(a):
    return (a - 32)  / 1.8 
def ftok(a):
    return 273.5 + ftoc(a)
def ktof(a):
    return 1.8*(ctok(a)) + 32
while 1:
    ans=0
    print("1.conversion 2.list-history 3.exit")
    n=int(input("enter your choice"))    
    if n==1:
        a=input("enter value with unit")
        b=input("enter unit to convert into").lower()
        c=a[-1].lower()
        val=float(a[:-1])
        print(b)
        if(c=='f' and b=='k'):
            ans=ftok(val)
        elif c=='f' and b=='c':
            ans=ftoc(val)
        elif(c=='c' and b=='k'):
            ans=ctok(val)
        elif c=='c' and b=='f':
            ans=ctof(val)
        elif(c=='k' and b=='c'):
            ans=ktoc(val)
        elif c=='k' and b=='f':
            ans=ktof(val)
        elif c==b:
            ans=val
        else:
            print("invalid input")    
        print("Ans:",ans,b)
        x=[val,c,"to",round(ans,3),b]
        history.append(tuple(x))
    elif n==2:
        print("1.from-unit 2.to-unit ")
        c=int(input("enter your choice"))
        if c==1:
            print(*sorted(history,key=lambda x:x[0]),sep="\n")
        elif c==2:
            print(*sorted(history,key=lambda x:x[3]),sep="\n")    
        else:
            print("invalid input")    
    else:
        break         