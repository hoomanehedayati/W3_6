print("Program starting.\nWelcome to the unit converter program!\nFollow the menu instructions below.\n\nOptions:\n1 - Length\n2 - Weight\n0 - Exit\n")

choice = int(input("Your choice:"))

if choice == 1:

    print("Length options:\n1 - Meters to kilometers\n2 - Kilometers to meters\n0 - Exit")

    choicelength = int(input("Your choice:"))

    if choicelength == 1:

        meters = float(input("Insert meters:"))

        mtok = round(meters / 1000,1)

        print(f'{meters} m is {mtok} km')

    elif choicelength == 2:

        kilometers = float(input("Insert kilometers:"))

        ktom = round(kilometers * 1000,1)

        print(f'{kilometers} km is {ktom} m')

    elif choicelength == 0:

        print("Exiting...")

    else:

        print("Unknown option.")

elif choice == 2:

    print("Weight options:\n1 - Grams to pounds\n2 - Pounds to grams\n0 - Exit")

    choiceweight = int(input("Your choice:"))

    if choiceweight == 1:

        grams = float(input("Insert grams:"))

        gtop = round(grams / 453.6,4)

        print(f'{grams} g is {gtop} lb')

    elif choiceweight == 2:

        pounds = float(input("Insert pounds:"))

        ptog = round(pounds * 453.6,1)

        print(f'{pounds} lb is {ptog} g')

    elif choiceweight == 0:

        print("Exiting...")

    else:

        print("Unknown option.")

elif choice == 0:

    print("Exiting...")

else:

    print("Unknown option.")

print("Program ending.")