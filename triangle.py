
class NotValidFigure(Exception): #Такого треугольника не существует
    pass

class Triangle:
    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if not self.is_valid():
            raise Exception

    def perimetr(self) -> float: 
        return round(self.side_a + self.side_b + self.side_c, 2)

    def ploshad(self) -> float: 
        p = (self.side_a + self.side_b + self.side_c) / 2
        return round(p*(p - self.side_a)*(p - self.side_b)*(self.side_c)**0.5 , 2)

    
    def is_valid(self) -> float:
        sides = [self.side_a, self.side_b, self.side_c]
        if all([isinstance(side,(int, float)) for side in sides]): #проверка являются-ли введённыеи данные числом 
            if all ([side >= 0 for side in sides]): #прохожимя по стороне списка
                #Функция all() возвращает значение True , если все элементы в итерируемом объекте - истинны
                # в противном случае она возвращает значение False.
                # isistance Возвращает True, если указанный объект является экземпляром указанного класса (классов), либо наследующегося от него класса
                # for side in sides включеиние 
                sorted_sides = sorted(sides) #сортруем от меньшего к большему  чтобы была возможность проверить с помошью посдеднегт жлемента меньше сумму двух жругих
                return sorted_sides[-1] < sorted_sides[0] + sorted_sides[1] #последняя сторона в списке нетдолжна быть больше чем сумма 
                #двух предыдщих если она будет больше то треугольник существовать не может 
                # Треугольник существует только тогда, когда сумма двух его сторон больше третьей.
                #  Требуется сравнить одну сторону с суммой двух других. 
                # Если хотя бы в одном случае сторона окажется больше либо равна сумме двух других, 
                # то треугольника с такими сторонами не существует.
                #если сумма пеервых двух элементов больше  чем значение  3  в списке то такого треугольника существовать не может

trian = Triangle(5, 10, 12)
print(trian.perimetr())
print(trian.ploshad())































#for side in sides включение
# если сумма пеервых двух больше либо равно чем 3 значеиние в списке то такого треугольника не существует 