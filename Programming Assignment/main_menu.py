def main_menu():
    while True:
        print("\n=== KZN Parking Management System ===")
        print("1. Customer")
        print("2. Parking Administrator")
        print("3. Shareholder")
        print("4. Exit")

        choice = int(input("Enter your Selection"))

        if choice == 1:
            print("Customer section coming right next")
            break

        elif choice == 2:
            print("Parking Administrator section right next")
            break

        elif choice == 3:
            print("Shareholder section coming right next")
            break

        elif choice == 4:
            print("System closed")
            break

        else:
            print("Invalid choice. Try again.")

main_menu()
