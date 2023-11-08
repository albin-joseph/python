#In this section we are going to learn more about Inheritance and slicing
class Animal:
    def __init__(self) -> None:
        self.number_eyes = 2
    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
        
    def swim(self):
        print("Moving in water")
        
nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.number_eyes)