#In this section we are going to learn more about OOP concept.
#An object have attributes and methods
class Vehicle:
    wheel = 4
    def start(self):
        print(f"Start rolling on {self.wheel} wheel")
        
car = Vehicle()
print(car.start())