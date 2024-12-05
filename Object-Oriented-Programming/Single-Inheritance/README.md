# Single Inheritance Example in Python

## Overview
This example demonstrates single inheritance in Python, showcasing how a `Developer` class inherits from a `Manager` class.

## Class Structure

### Manager Class
Base class with core employee information and methods:
- Attributes:
  - `name`: Employee's name (string)
  - `age`: Employee's age (integer)
  - `company`: Company name (string)
  - `position`: Job position (string)
  - `salary`: Employee's salary (float)

- Methods:
  - `display_info()`: Prints basic employee information
  - `calculate_bonus()`: Calculates bonus based on salary percentage

### Developer Class
Inherits from Manager class with additional functionality:
- Additional Attribute:
  - `languages`: List of programming languages

- Overridden/Extended Methods:
  - `display_all_details()`: Displays all information from parent class and additional details

## Key Inheritance Concepts Demonstrated

### 1. `super()` Usage
- `super().__init__()`: Calls the parent class's constructor
- Allows inheriting and initializing parent class attributes
- Enables extending the initialization process

### 2. Method Overriding
- `display_all_details()` method extends the parent's `display_info()` method
- Adds additional information about programming languages

### 3. Attribute Extension
- Adds `languages` attribute specific to the Developer class
- Maintains all attributes from the Manager class

## Example Usage
```python
dev = Developer(
    name="M:Huzaifa", 
    age=30, 
    company="XYZ Corp", 
    position="Agentic Developer", 
    salary=100000, 
    percentage=10, 
    languages=["Python", "Java", "C++", "TypeScript", "JavaScript"]
)
dev.display_all_details()
```

## Best Practices
- Use `super()` to properly initialize parent class
- Extend functionality without modifying parent class
- Keep inheritance hierarchies simple and logical
- Use type hints for better code readability

## Potential Improvements
- Add error handling
- Implement more sophisticated bonus calculation
- Add method to update or modify attributes