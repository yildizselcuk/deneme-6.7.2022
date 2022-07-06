print("WELCOME")
num1 = input("enter a number: ")
num2 = input("enter a number: ")
sign = input("choose sign symbol")
if sign == "*":
    print(float(num1)*float(num2))
elif sign == "/":
    print(float(num1) / float(num2))
elif sign == "+":
    print(float(num1) + float(num2))
elif sign == "-":
    print(float(num1) - float(num2))
else:
    print("wrong symbol please chose mathematical symbols *+-/")


