# a funtion for the calculator
def calc():
    # print the prompts for user
    print('Pick which mathematical operation you want to use\n')
    print('1.Addition\n2.subtraction\n3.multiplication\n4.dividion\n')
    # tell user to select/enter their desired math operation they want to use
    method = input("Enter: ")
    # prompt user to enter the first and second number
    num1 = input('Enter the first number: ')
    num2 = input('Enter the second number: ')
    # note I do know that they would have to enter the num1 and num2 either way even if they enter something
    # beside 1-4 but didn't have time to change

    # base on what they've enter for method, convert it to int and match it with if statements
    # 1 for additon
    if int(method) == 1:
        print(int(num1)+int(num2))
    # 2 for subtraction
    elif int(method) == 2:
        print(int(num1)-int(num2))
    # 3 for multiplication
    elif int(method) == 3:
        print(int(num1)*int(num2))
    # 4 for division
    elif int(method) == 4:
        print(int(num1)/int(num2))
    # if they enter anything else, print this line
    else:
        print("Wasn't one of the options")


calc()
