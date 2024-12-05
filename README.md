# Modern Python Assignments

## Type Annotations
```python
# Traditional Assignment
name = "John Doe"
age = 30

# Modern Type-Annotated Assignment
name: str = "John Doe"
age: int = 30

# Function with Type Hints
def greet(name: str, age: int) -> str:
    return f"Hello, {name}. You are {age} years old."
```

## Unpacking Assignments
```python
# Multiple Assignment
x, y, z = (1, 2, 3)

# Extended Unpacking
first, *middle, last = [1, 2, 3, 4, 5]
# first = 1, middle = [2, 3, 4], last = 5

# Dictionary Unpacking
person = {"name": "Alice", "age": 30, "city": "New York"}
name, **details = person
```

## Walrus Operator (:=)
```python
# Inline Assignment and Condition
if (n := len([1, 2, 3])) > 2:
    print(f"List has {n} elements")

# Reducing Repeated Calculations
while (chunk := file.read(1024)):
    process(chunk)
```

## Pattern Matching (Python 3.10+)
```python
def process_data(data):
    match data:
        case {"type": "user", "name": name}:
            return f"User: {name}"
        case [*rest] if len(rest) > 2:
            return f"Long list: {rest}"
        case _:
            return "Unknown data"
```

## Advanced Assignment Techniques
```python
# Conditional Expressions
status = "Active" if is_active else "Inactive"

# Dictionary Comprehensions
squares = {x: x**2 for x in range(6)}

# Object Attribute Assignment
class Person:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
```

## Best Practices
- Use type annotations for clarity
- Leverage unpacking for concise assignments
- Employ walrus operator for inline logic
- Utilize pattern matching for complex conditionals
- Prefer comprehensions over traditional loops

## Performance Considerations
- Type annotations have minimal runtime overhead
- Walrus operator can improve readability and performance
- Comprehensions are generally faster than equivalent loops

## Tools and Linters
- mypy: Static type checker
- pylint: Code quality tool
- black: Code formatter supporting modern syntax
