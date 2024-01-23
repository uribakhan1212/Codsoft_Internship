while True:
    op1 = input("Please enter the first operand: ")
    op2 = input("Please enter the second operand: ")    
    x = input("Please enter the operation to be performed: ")    
    result = 0
    if x == '*':
        result = float(op1)*float(op2)

    elif x == '+':
        result = float(op1)+float(op2)

    elif x == '-':
        result = float(op1)-float(op2)

    elif x == '/':
        result = float(op1)/float(op2)
    print("The result of {} {} {} is {}".format(op1, x, op2, result))    
    choice = input("Do you want to continue? Y/N: ")
    if choice == "y" or choice == "Y":
        continue
    else:
        break 
