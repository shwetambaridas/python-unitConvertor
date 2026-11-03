print("CHOOSE THE CONVERSION TYPE")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Kilometers to Miles")
print("4. Miles to Kilometers")

choice = int(input("Enter your choice (1-4) : "))

if choice == 1:
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choice == 2:
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C")
elif choice == 3:
    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometers * 0.621371
    print(f"{kilometers} km is equal to {miles} miles")
elif choice == 4:
    miles = float(input("Enter distance in miles: "))
    kilometers = miles / 0.621371
    print(f"{miles} miles is equal to {kilometers} km")
else:
    print("Invalid choice")