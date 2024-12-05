# Single Inheritance

class Manager:
    def __init__(self,name:str,age:int,company:str,position:str,salary:float):
        self.name:str = name
        self.age:int = age
        self.company:str = company
        self.position:str = position
        self.salary:float = salary
       
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Company: {self.company}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")
    
    def calculate_bonus(self, percentage:float=20):
        bonus = self.salary * percentage / 100
        print("Bonus",bonus)

class Developer(Manager):
    def __init__(self, name:str, age:int, company:str, position:str, salary:float, percentage:float, languages:list):
        super().__init__(name, age, company, position, salary)
        self.languages:list = languages

    def display_all_details(self):
        super().display_info()
        super().calculate_bonus()
        print("Languages:", ", ".join(self.languages))
    

#create object

dev = Developer("M:Huzaifa", 30, "XYZ Corp", "Agentic Developer", 100000, 10, ["Python", "Java", "C++","TypeScript", "JavaScript"])
dev.display_all_details()
        