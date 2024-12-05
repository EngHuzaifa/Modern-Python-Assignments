# Multi-Level-Inheritance

class Vehicle:
    def __init__(self,make:str,model:int,year:int):
        self.make=make
        self.model=model
        self.year=year
    
    def display_info(self):
        print(f"""Make :{self.make} 
                  Model :{self.model}
                  Year :{self.year}""")

class Car(Vehicle):
    def __init__(self,make:str,model:int,year:int,num_doors:int,fuel_type:str):
        super().__init__(make, model, year)
        self.num_doors=num_doors
        self.fuel_type=fuel_type
    
    def Car_details(self):
        print(f"""Number of Car Doors :{self.num_doors}
                  Fuel Type :{self.fuel_type}""")

class ElectricCar(Car):
    def __init__(self,make:str,model:int,year:int,num_doors:int,fuel_type:str,battery_capacity:int,range_per_charge:int):
        super().__init__(make,model,year,num_doors,fuel_type)
        self.battery_capacity=battery_capacity
        self.range_per_charge=range_per_charge
    
    def electric_car_details(self):
        print(f"""Battery Capacity :{self.battery_capacity}
                  Range per Charge :{self.range_per_charge} miles""")
        
    def show(self):
        self.display_info()
        self.Car_details()
        self.electric_car_details()

#create object

obj:ElectricCar=ElectricCar("Electric",24,2024,4,"petrol",150,200)
obj.show()
    