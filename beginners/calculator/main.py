# Mathematical Operators

# User will select operator (+ - * /) and input two values when prompted.
# Value of two values will be calculated based on operand selected.

operand = input("Select operator: (+ - * /"))
num1 = float(input("Enter value 1: ")) # typecast as float for more complex calculations
num2 = float(input("Enter value 2: "))

if operand == "+":
  print(num1 + num2)
elif operand == "-":
  print(num1 - num2)
elif operand == "*":
  print(num1 * num2)
elif operand == "/":
  print(num1 / num2)



