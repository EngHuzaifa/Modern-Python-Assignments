from typing import Any

class Calculate:
    def __init__(self, num1: Any, num2: Any):
        self.num1 = num1
        self.num2 = num2

    def add(self) -> Any:
        if isinstance(self.num1, int) and isinstance(self.num2, int):
            return self.num1 + self.num2
        elif isinstance(self.num1, float) and isinstance(self.num2, float):
            return self.num1 + self.num2
        elif isinstance(self.num1, complex) and isinstance(self.num2, complex):
            return self.num1 + self.num2
        elif isinstance(self.num1, str) and isinstance(self.num2, str):
            return self.num1 + self.num2
        else:
            raise TypeError("Unsupported types for addition")

class Results(Calculate):
    def show(self):
        try:
            result = self.add()
            print(f"The result of adding {self.num1} and {self.num2} is: {result}")
        except TypeError as e:
            print(e)

# Testing with different types
calc_int = Results(10, 20)
calc_int.show()

calc_float = Results(10.5, 20.3)
calc_float.show()

calc_complex = Results(3 + 4j, 1 + 2j)
calc_complex.show()

calc_str = Results("Hello, ", "World!")
calc_str.show()

#calc_invalid = Results(10, "20")
#calc_invalid.show()  # This will raise a TypeError
