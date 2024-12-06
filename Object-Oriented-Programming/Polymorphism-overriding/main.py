class PartTimeWorker():
    def __init__(self, hourly_rate:int, hours_worked:int):
        self.hourly_rate:int = hourly_rate
        self.hours_worked:int = hours_worked
    
    def calculate_pay(self):
        print(f"Calculating part time salary :${self.hourly_rate*self.hours_worked}")
    
    def show_details_parttimeworker(self):
        print(f"Hourly rate :${self.hourly_rate}")
        print(f"Hours worked :${self.hours_worked}")

class Frelancer(PartTimeWorker):
    def __init__(self, hourly_rate:int, hours_worked:int, ProjectCount:int,PayPerProject:int):
        super().__init__(hourly_rate, hours_worked)
        self.ProjectCount:int = ProjectCount
        self.PayPerProject:int = PayPerProject
    
    def calculate_pay(self):
        print(f"Calculating freelancer salary :${self.ProjectCount*self.PayPerProject}")
    
    def show_details_frelancer(self):
        print(f"Number of projects :${self.ProjectCount}")
        print(f"Pay per project :${self.PayPerProject}")

class HybridWorker(Frelancer):
    def __init__(self, hourly_rate:int, hours_worked:int, ProjectCount:int, PayPerProject:int):
        super().__init__(hourly_rate, hours_worked, ProjectCount, PayPerProject)
    
    def Totall_Earning(self):
        super().calculate_pay
       
    def show(self):
        super().show_details_parttimeworker()
        super().show_details_frelancer()
        print(f"Total earning :${self.hourly_rate*self.hours_worked+self.ProjectCount*self.PayPerProject}")
    


worker:HybridWorker=HybridWorker(1000,4300,10000,50000)
worker.show()
worker.Totall_Earning()