# Weight Converter

weight = float(input("Enter weight: "))
unit = input("Is weight measured in kilograms or pounds? (Enter kg or lb): ")

if unit == "kg":
  weight = weight * 2.205
  print(f"Your weight is: (round{weight, 2} {unit}") # round function added, unit will be round to 2 decimal places
elif unit == "lb":
  weight = weight / 2.205
  print(f"Your weight is: (round{weight, 2} {unit}") # round function added, unit will be round to 2 decimal places
else:
  print(f"{unit} isn't valid")


