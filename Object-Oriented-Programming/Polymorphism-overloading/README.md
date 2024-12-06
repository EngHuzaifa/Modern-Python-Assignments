# Polymorphic Addition Calculator

## Overview
This Python script demonstrates a polymorphic approach to addition using runtime type checking. The implementation allows for adding different types of data within a single method.

## Features
- Supports addition for multiple types:
  - Integers
  - Floating-point numbers
  - Complex numbers
  - Strings
- Dynamic type checking
- Error handling for incompatible types

## Class Structure

### 1. Calculate Class
A base class designed to perform type-checked addition.

#### Attributes
- `num1`: First value to be added
- `num2`: Second value to be added

#### Methods
- `add()`: 
  - Performs addition based on input types
  - Supports multiple data types
  - Raises `TypeError` for unsupported type combinations

### 2. Results Class
Extends the Calculate class to display addition results.

#### Methods
- `show()`:
  - Calls `add()` method
  - Prints the result of addition
  - Handles potential type errors

## Usage Examples

```python
# Integer addition
calc_int = Results(10, 20)
calc_int.show()
# Output: The result of adding 10 and 20 is: 30

# Float addition
calc_float = Results(10.5, 20.3)
calc_float.show()
# Output: The result of adding 10.5 and 20.3 is: 30.8

# Complex number addition
calc_complex = Results(3 + 4j, 1 + 2j)
calc_complex.show()
# Output: The result of adding (3+4j) and (1+2j) is: (4+6j)

# String concatenation
calc_str = Results("Hello, ", "World!")
calc_str.show()
# Output: The result of adding Hello,  and World! is: Hello, World!
```

## Error Handling
- Attempting to add incompatible types will raise a `TypeError`
- The `show()` method catches and displays these errors

## Limitations
- Only supports addition
- Limited to specific types (int, float, complex, str)
- Requires manual type checking


## Python Version Compatibility
- Requires Python 3.6+
- Uses type hinting
