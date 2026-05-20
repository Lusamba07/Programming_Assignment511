def customer_menu():
    while True:
        print("\n--- CUSTOMER MENU ---")
        print("1. Registration")
        print("2. Sign_in")
        print("3. Mall Selection")
        print("4. Vehicle Entry")
        print("5. Vehicle Exit")
        print("6. Payment")
        print("7. Back")

        choice = int(input("Choose: "))


def mall_selection():
    print("1. Tyger Valley Shopping Centre")
    print("2. V&A Waterfront")
    print("3. N1 City Mall")
    print("4. Canal Walk Shopping Centre")
    print("4. Kenilworth Centre")


mall = input("Select Mall: ")

print("Mall selected successfully")


def vehicle_entry():
    car = input("Enter car registration: ")

    with open("parking.txt", "a") as file:
        file.write(car + "\n")

    print("Vehicle entered successfully")
