unit = input("Is this temperature in celsius or fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))  

if unit.upper() == "C":
    converted_temp = (temp * 9/5) + 32
    print(f"The temperature in Fahrenheit is {converted_temp}°F.")
elif unit.upper() == "F":
    converted_temp = (temp - 32) * 5/9
    print(f"The temperature in Celsius is {converted_temp}°C.")
else:
    print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
