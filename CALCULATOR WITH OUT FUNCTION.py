flag="print"
print("*********  Welcome to the ZOdiac calculator  **************")
print("enter number1 : ")
num1=int(input())
print("enter the number 2 :")
num2=int(input())
print("these are the operators you can use :")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Divison")
print("5. Modulus")
result = 0
operator = input("please choose an option from these (1,2,3,4,5):")
if operator == "1":
    result = num1+num2
    print("The result of a addition of",num1, "and" ,num2,"is", result)
if operator == "2":
    if num1<num2:
        print("cannot substract the first number is less than the second number")
    else:
        result=num1-num2
        print("the result of a substraction of",num1,"and",num2,"is",result)
if operator == "3":
    if num2==0 or num1==0: #any number(2,1)
        print("can not multipli by zero")
    else:
        result = num1*num2
        print("The result of multiplication of",num1,"and",num2,"is",result)
if operator == "4":
    if num2==0:
        print("can not divide by zero")
    else:
        result=num1//num2
        print("The result of division of",num1, "and" ,num2,"is",result)
if operator == "5":
    if num2==0:
        print("can not divide by zero")
    else:
        result = num1%num2
        print("the result of modulus of",num1,"and",num2,"is",result)

