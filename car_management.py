from car import Car

def main():
    while True:
        print("\nCar Management System")
        print("1. Add a car")
        print("2. View all cars")
        print("3. View total number of cars")
        print("4. See a car's details")
        print("5. Service a car")
        print("6. Update mileage")
        print("7. Quit\n")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            Car.add_car()
        elif choice == '2':
            all_cars = Car.view_all_cars()
            for car_id, car_ in all_cars.items():
                print(f"ID: {car_id}, Make: {car_._make}, Model: {car_._model}, Year: {car_._year}, Mileage: {car_._mileage}")
        elif choice == '3':
            total_cars = Car.view_total_cars()
            print(f"Total number of cars: {total_cars}")
        elif choice == '4':
            car_id = input("Enter the car ID to view details: ")
            details = Car.view_car_details(int(car_id))
            if isinstance(details, dict):
                for key, val in details.items():
                    print(f"{key}: {val}")
            else:
                print(f"No car found with ID: {car_id}")
        elif choice == '5':
            car_id = input("Enter the car ID to service: ")
            car = Car.all_cars.get(int(car_id))
            if car:
                service = input("Enter the service performed: ")
                added_service = car.add_service(service)
                print(f"Service '{added_service}' added to car ID {car_id}.")
            else:
                print(f"No car found with ID: {car_id}")
        elif choice == '6':
            car_id = input("Enter the car ID to update mileage: ")
            car = Car.all_cars.get(int(car_id))
            if car:
                try:
                    new_mileage = int(input("Enter the new mileage: "))
                    updated_mileage = car.update_mileage(new_mileage)
                    print(f"Mileage updated to {updated_mileage} for car ID {car_id}.")
                except ValueError as e:
                    print(e)
            else:
                print(f"No car found with ID: {car_id}")
        elif choice == '7':
            print("Exiting the Car Management System...Have a most excellent day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
        
if __name__ == "__main__":
    main()