#calculator

while True:
    print("+ for addition")
    print("- for substraction")
    print("* for multiplication")
    print("/ for division")
    print("** for power")
    print("% for modulo")
    print("// for floor division")
    print("E for exit")
    ch=input("Enter your choice")
    if ch=='+':
        a=int(input("Enter value for a=>"))
        b=int(input("Enter value for b=>"))
        s=a+b
        print("addition of {} + {} is {}".format(a,b,s))
    elif ch=='-':
        a=int(input("Enter value for a=>"))
        b=int(input("Enter value for b=>"))
        s=a-b
        print("substraction of {} - {} is {}".format(a,b,s))
    elif ch=='*':
        a=int(input("Enter value for a=>"))
        b=int(input("Enter value for b=>"))
        s=a*b
        print("multiplication of {} * {} is {}".format(a,b,s))
    elif ch=='/':
        a=int(input("Enter value for a=>"))
        b=int(input("Enter value for b=>"))
        s=a/b
        print("division of {} / {} is {}".format(a,b,s))
    elif ch=='**':
        a=int(input("Enter value for a=>"))
        b=int(input("Enter value for b=>"))
        s=a**b
        print("power of {} ** {} is {}".format(a,b,s))
    elif ch=='%':
        a=int(input("Enter value for a=>"))
        b=int(input("Enter value for b=>"))
        s=a%b
        print("modulo of {} % {} is {}".format(a,b,s))
    elif ch=='//':
        a=int(input("Enter value for a=>"))
        b=int(input("Enter value for b=>"))
        s=a//b
        print("floor division of {} // {} is {}".format(a,b,s))
    elif ch=='E':
        break
    else:
        print("Invalid choice")
    cha=input("Do you want to perform more calculations (y/n) =>")
    if cha=='Y' or cha=='y':
        continue
    else:
        break
    else:
        print("No such a operation")
    
            
