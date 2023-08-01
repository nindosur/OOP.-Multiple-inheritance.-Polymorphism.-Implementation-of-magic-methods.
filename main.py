import math
    # 1, 2
class Shape:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'Название фигуры: {self.name}'
    def square(self):
        pass

class Rectangle(Shape):  # S = a*b
    def __init__(self, a, b):
        super().__init__("Прямоугольник")
        self.a = a
        self.b = b
    def square(self):
        return self.a * self.b
    def __int__(self):
        return int(self.a * self.b)
    def __str__(self):
        return(f'Имя фигуры: {self.name} \nПлощадь: {Rectangle.__int__(self)}')

class Circle(Shape):  # S = (radius**2)* pi
    def __init__(self, radius):
        super().__init__("Круг")
        self.radius = radius
    def square(self):
        return (self.radius**2)*math.pi
    def __int__(self):
        return int((self.radius**2)*math.pi)
    def __str__(self):
        return(f'Имя фигуры: {self.name} \nПлощадь: {Circle.__int__(self)}')

class right_triangle(Shape): # S = 1/2*bh
    def __init__(self, b, h):
        super().__init__("Прямоугольный треугольник")
        self.b = b
        self.h = h
    def square(self):
        return 1/2 * self.h * self.b
    def __int__(self):
        return int(1/2 * self.h * self.b)
    def __str__(self):
        return(f'Имя фигуры: {self.name} \nПлощадь: {right_triangle.__int__(self)}')

class trapezoid(Shape): # S = 1/2 * h * (a+b)
    def __init__(self, h, a, b):
        super().__init__("Трапеция")
        self.h = h
        self.a = a
        self.b = b
    def square(self):
        return 1/2 * self.h * (self.a + self.b)
    def __int__(self):
        return int(1 / 2 * self.h * (self.a + self.b))
        # return int(trapezoid.square())
    def __str__(self):
        return(f'Имя фигуры: {self.name} \nПлощадь: {trapezoid.__int__(self)}')

rect = Rectangle(2, 5)
circle = Circle(60)
rt = right_triangle(5, 10)
trape = trapezoid(2, 5, 10)

for class1 in (rect, circle, rt, trape):
    print('*'*11)
    print(f'{class1}')

    # 3
class Shape:
    def __init__(self, name):
        self.name = name
    def Show(self):
            return f"Название: {self.name}"
    def Save(self):
        with open("test1.txt", "w") as f:
            f.write(self.name)
    def Load(self):
        with open("test1.txt") as f:
            a = f.readline()
        print(a)

class Square(Shape):
    def __init__(self):
        super().__init__("Square")
    def Show(self):
            return f"Название: {self.name}"
    def Save(self):
        with open("test1.txt", "w") as f:
            f.write(self.name)
    def Load(self):
        with open("test1.txt") as f:
            a = f.readline()
        print(a)

class Rectangle(Shape):
    def __init__(self):
        super().__init__("Rectangle")
    def Show(self):
            return f"Название: {self.name}"
    def Save(self):
        with open("test1.txt", "w") as f:
            f.write(self.name)
    def Load(self):
        with open("test1.txt") as f:
            a = f.readline()
        print(a)

class Circle(Shape):
    def __init__(self):
        super().__init__("Circle")
    def Show(self):
            return f"Название: {self.name}"
    def Save(self):
        with open("test1.txt", "w") as f:
            f.write(self.name)
    def Load(self):
        with open("test1.txt") as f:
            a = f.readline()
        print(a)

class Ellipse(Shape):
    def __init__(self):
        super().__init__("Ellipse")
    def Show(self):
        return f"Название: {self.name}"
    def Save(self):
        with open("test1.txt", "w") as f:
            f.write(self.name)
    def Load(self):
        with open("test1.txt") as f:
            a = f.readline()
        print(a)

square = Square()
rect = Rectangle()
circle = Circle()
ellip = Ellipse()
for i in (square, rect, circle, ellip):
    i.Save()
    i.Load()