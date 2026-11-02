class Car:
    all_cars = {}
    total_cars = len(all_cars.keys())
    # class-level counter to ensure unique, increasing IDs (auto-increment)
    _id_counter = 0
    
    def __init__(self, make, model, year, mileage):
        self._id = self.generate_id()  # Generate a unique ID for each car instance
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = []
    
    @classmethod
    def generate_id(cls):
        cls._id_counter += 1
        return cls._id_counter
    
    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, val):
        if not isinstance(val, str):
            raise ValueError("Make must be a string.")
        self._make = val.strip().title()
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, val):
        if not isinstance(val, str):
            raise ValueError("Model must be a string.")
        self._model = val.strip().title()
    
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, val):
        if not isinstance(val, int):
            raise ValueError("Year must be an integer.")
        self._year = val

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, val):
        if not isinstance(val, int):
            raise ValueError("Mileage must be an integer.")
        self._mileage = val
    
    def add_service(self, service):
        if not isinstance(service, str):
            raise ValueError("Service must be a string.")
        self._services.append(service.strip().title())
        return self._services[-1]  # Return the last added service for confirmation
        
    @classmethod
    def add_car(cls) -> 'Car':
        new_car = {
            "make": input("Enter car make: "),
            "model": input("Enter car model: "),
            "year": int(input("Enter car year: ")),
            "mileage": int(input("Enter car mileage: "))
        }
        car = cls(**new_car)
        cls.all_cars[car._id] = car
        cls.total_cars = len(cls.all_cars.keys()) # update total_cars whenever a new car is added
        print(f"Car added successfully! Total cars: {cls.total_cars}.")
        return car
    
    @classmethod
    def view_all_cars(cls):
        return cls.all_cars
    
    @classmethod
    def view_total_cars(cls):
        return cls.total_cars

    @classmethod
    def view_car_details(cls, car_id):
        car = cls.all_cars.get(car_id)
        if car:
            return {
                "ID": car._id,
                "Make": car._make,
                "Model": car._model,
                "Year": car._year,
                "Mileage": car._mileage,
                "Services": car._services
            }
        else:
            return f"No car found with ID: {car_id}"
        
    def update_mileage(self, new_mileage):
        if not isinstance(new_mileage, int):
            raise ValueError("Mileage must be an integer.")
        self._mileage = new_mileage
        return self._mileage

        
    
'''
```bash
----  WELCOME  ----
1. Add a car
2. View all cars
3. View total number of cars
4. See a car's details
5. Service a car
6. Update mileage
7. Quit
```
'''