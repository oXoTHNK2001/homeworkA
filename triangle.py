class Triangle:
    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def ploshad(self) -> float: 
        p = (self.side_a + self.side_b + self.side_c) / 2
        return (p*(p - self.side_a)*(p - self.side_b)*(self.side_c))**0.5 

    def perimetr(self) -> float: 
        return self.side_a + self.side_b + self.side_c

trian = Triangle(7, 7, 7)
print(trian.perimetr())
print(trian.ploshad())
