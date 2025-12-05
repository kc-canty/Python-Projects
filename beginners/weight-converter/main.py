# Weight Converter

weight = float(input("Enter weight: "))
unit - input("Is weight in kilograms or pounds? (kg or lb)")

if unit == "kg":
  weight = weight * 2.205
elif unit == "lb":
  weight = weight / 2.205
else:
  print(f"{unit} isn't valid")

print(f:"Your weight is: {weight} {}")
