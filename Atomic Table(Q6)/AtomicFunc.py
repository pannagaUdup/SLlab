def atomicop():    
    dict={'Na':'sodium','Fe':'iron','Cu':'copper'}
    while 1:
        print('1:insert-element 2.LengthOfTable 3.GetElement 4.exit')
        n=int(input("enter your choice "))
        if n==1:
            a,b=input("enter element symbol and name to insert ").split(" ")
            dict[a]=b
            print(dict)
        elif n==2:
            print("length is",len(dict))
        elif n==3:
            a=input("enter symbol ")
            print(dict[a])
        else:
            break  