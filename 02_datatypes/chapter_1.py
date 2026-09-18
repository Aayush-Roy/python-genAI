num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
opr = input("Enter opr: ");

if opr == '+':
    print(f"Sum is {num1+num2}")
elif opr == '-':
    print(f"Difference is {num2-num1}")
elif opr == '*':
    print(f"Multiplies is {num1*num2}")
else :
    print("Invalid Operator!!")
