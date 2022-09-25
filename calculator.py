
num1 = int(input ("enter the first number"))
operator = input("enter an operator")
num2 = int(input("enter the second number"))


if (operator == '+'):
    result = num1 + num2
    print("the result is: "+ str(result))
elif (operator == '-'):
    result = num1 - num2
    print("the result is: "+ str(result))
elif (operator == '*'):
    result = num1 * num2 
    print("the result is: "  + str(result))
elif (operator== '/'):
    if (num2 == 0):
        print("invalid operation")
    else:    
        result = num1 / num2 
        print("the result is: "+ str(result))
        print("this is a test")
        print("hello this is new branch")
        print("hello this is new branch 2")

