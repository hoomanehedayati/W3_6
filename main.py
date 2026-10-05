print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.\n")
print("Options:\n1 - Length\n2 - Weight\n0 - Exit")
choice = int(input("Your choice: "))

if choice == 1:
    print("\nLength options:\n1 - Meters to kilometers\n2 - Kilometers to meters\n0 - Exit")
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
    print("\nWeight options:\n1 - Grams to pounds\n2 - Pounds to grams\n0 - Exit")
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
    print("\nExiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")