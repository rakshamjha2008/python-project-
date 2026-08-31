#calculator

a = float(input("Enter the first num: "))
b = float(input("Enter the second num: "))
op = input("Enter operator (+, -, *, /, %, **): ")

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
elif op == '**':
    print(a ** b)
elif op == '%':
    op == '%'
else:
    print("invalid operator")
