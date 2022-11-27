import math

class Circle:
    def __init__(self, radius: float) -> None: 
        self.radius = radius

    def dlina(self) -> float:
        return 2 * math.pi * self.radius
    
    def ploshad(self) -> float:
        return math.pi * self.radius ** 2

circ = Circle(4)
print(circ.dlina())
print(circ.ploshad())



