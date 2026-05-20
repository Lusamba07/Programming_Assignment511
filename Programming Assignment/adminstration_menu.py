def administration_menu():
    while True:
        print("\n--- Administration Menu ---")
        print("1. View Parked Vehicles")
        print("2. Verify Parking Capacity")
        print("3. Daily Parking Report")
        print("4. Back to Main Menu")

        choice = int(input("Choose option: "))

    def view_parked_vehicles():
        try:
    with open("parking.txt", "r") as file:
                cars = file.readlines()

                if len(cars) == 0:
                    print("\n No vehicles are currently parked.\n")
                else:
                    print("\n --- Parked Vehicles ---")
                    for car in cars:
                        print(car.strip())

        except FileNotFoundError:
            print("\n parking.txt file not found.\n")

    def verify_parking_capacity():
        total_spaces = 150

        try:
            with open("parking.txt", "r") as file:
                cars = file.readlines()
                used_spaces = len(cars)
                available_spaces = total_spaces - used_spaces

                print("\n --- Parking Capacity ---")
                print("Total Parking Spaces:", total_spaces)
                print("Used Spaces:", used_spaces)
                print("Available Spaces:", available_spaces)

        except FileNotFoundError:
            print("\n parking.txt file not found. \n")


