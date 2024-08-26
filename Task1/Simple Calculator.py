ch=0
while ch<5:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))

    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        c=a+b
        print("Sum:",c)
        print('\n')
    elif ch==2:
        c=a-b
        print("Difference:",c)
        print('\n')
    elif ch==3:
        c=a*b
        print("product:",c)
        print('\n')
    elif ch==4:
        if a>b:
            c=a/b
            print("quotient:",c)
            print('\n')
        else:
            print("cannot divide")
            print('\n')
    elif ch==5:
        print("quiting...")
        break
    else:
        print("Invalid choice")
        print('\n')
            
    
        
               
           

