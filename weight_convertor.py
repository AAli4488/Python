weight = float(input("Enter your weight: "))
unit = input("Enter unit (K for kilogram or L for pound): ")

if unit.upper() == "K":
    converted_weight = weight * 2.20462
    print(f"Your weight is {converted_weight} pounds.")
elif unit.upper() == "L":
    converted_weight = weight / 2.20462
    print(f"Your weight is {converted_weight} kilograms.")
else:
    print("Invalid unit.")

print(f"Your weight is: {weight} {unit.upper()}")   