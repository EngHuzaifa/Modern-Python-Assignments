# Worker Classes Hierarchy

## Overview
This Python script defines a hierarchy of worker classes that demonstrate inheritance and polymorphism, representing different types of employment arrangements.

## Class Structure

### 1. PartTimeWorker
A base class representing part-time workers with basic pay calculation.

#### Attributes:
- `hourly_rate`: Rate of pay per hour
- `hours_worked`: Number of hours worked

#### Methods:
- `calculate_pay()`: Calculates total pay based on hourly rate and hours worked
- `show_details_parttimeworker()`: Displays worker's hourly rate and hours worked

### 2. Freelancer (Inherits from PartTimeWorker)
A class extending PartTimeWorker to include project-based work.

#### Additional Attributes:
- `ProjectCount`: Number of projects completed
- `PayPerProject`: Payment received per project

#### Additional Methods:
- `calculate_pay()`: Overrides base class method to calculate pay based on projects
- `show_details_frelancer()`: Displays project-related details

### 3. HybridWorker (Inherits from Freelancer)
A class combining part-time and project-based work.

#### Methods:
- `Totall_Earning()`: Calculates total earnings from both hourly and project-based work
- `show()`: Displays details from both part-time and freelance work

## Usage Example
```python
# Create a HybridWorker instance
worker = HybridWorker(hourly_rate=1000, hours_worked=4300, ProjectCount=10000, PayPerProject=50000)

# Display worker details and calculate earnings
worker.show()
worker.Totall_Earning()
```

## Note
- The class demonstrates multiple inheritance and method overriding
- Demonstrates how different types of workers can have varying pay calculation methods
