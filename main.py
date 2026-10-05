print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")
print()
print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice = int(input("Your choice: "))

if choice == 1:
    print()
    print("Length options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    sub = int(input("Your choice: "))
    if sub == 1:
        meters = float(input("Insert meters: "))
        km = meters / 1000
        print(f"{meters} m is {km} km")
    elif sub == 2:
        km = float(input("Insert kilometers: "))
        meters = km * 1000
        print(f"{km} km is {meters} m")
    elif sub == 0:
        print("Exiting...")
    else:
        print("Unknown option.")
elif choice == 2:
    print()
    print("Weight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    sub = int(input("Your choice: "))
    if sub == 1:
        grams = float(input("Insert grams: "))
        pounds = grams * 0.002205
        print(f"{grams} g is {pounds} lb")
    elif sub == 2:
        pounds = float(input("Insert pounds: "))
        grams = pounds * 453.6
        print(f"{pounds} lb is {grams} g")
    elif sub == 0:
        print("Exiting...")
    else:
        print("Unknown option.")
elif choice == 0:
    print()
    print("Exiting...")
else:
    print("Unknown option.")

print()
print("Program ending.")