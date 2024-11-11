def get_number(number):
    while True:
        operand = input("Number " + str(number) + ": ")
        try:
            return float(operand)
        except:
            print("Invalid number! Try again!")


operand1 = get_number(1)
sign = input("Sign: ")
operand2 = get_number(2)

result = 0
print (operand1, sign, operand2)
if sign == "+":
    result = (operand1) + (operand2)
elif sign == "-":
    result = (operand1) - (operand2)
elif sign == "*":
    result = (operand1) * (operand2)
elif sign == "/":
    if operand2 == "0":
        result = print("cannot be divided by zero")
    else:
        result = (operand1) / (operand2)
elif sign == "%":
    result = (operand1) % (operand2)
else:
    result = print("Invalid sign!")

print(result)
