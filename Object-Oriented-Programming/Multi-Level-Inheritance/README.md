# Multi-Level Inheritance Example in Python

## Overview
Demonstrates a three-level inheritance hierarchy representing vehicles, cars, and electric cars.

## Class Hierarchy

### 1. Base Class: Vehicle
- Attributes:
  - `make`: Manufacturer
  - `model`: Vehicle model
  - `year`: Manufacturing year
- Method: `display_info()` - Prints basic vehicle information

### 2. Derived Class: Car (Inherits from Vehicle)
- Additional Attributes:
  - `num_doors`: Number of car doors
  - `fuel_type`: Type of fuel used
- Method: `Car_details()` - Prints car-specific details

### 3. Final Class: ElectricCar (Inherits from Car)
- Additional Attributes:
  - `battery_capacity`: Battery capacity
  - `range_per_charge`: Driving range per charge
- Method: `electric_car_details()` - Prints electric car-specific details
- Method: `show()` - Displays all inherited and specific details

## Key Inheritance Concepts

### Method Resolution
- Uses `super()` to call parent class constructors
- Enables extending and specializing base class functionality
- Allows accumulation of attributes through inheritance levels

## Example Usage
```python
# Create an electric car object
obj = ElectricCar(
    make="Electric", 
    model=24, 
    year=2024, 
    num_doors=4, 
    fuel_type="petrol", 
    battery_capacity=150, 
    range_per_charge=200
)

# Display complete vehicle information
obj.show()
```

## Best Practices
- Use inheritance to model is-a relationships
- Keep inheritance hierarchies simple and logical
- Prefer composition when appropriate
- Use type hints for clarity


