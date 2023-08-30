# Превратите функции в методы класса, а параметры в свойства.(треугольник)

class Triangle:
    def __init__(self):
        self.a = float(input("Введите длину стороны a: "))
        self.b = float(input("Введите длину стороны b: "))
        self.c = float(input("Введите длину стороны c: "))

    def check_triangle(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            print("Треугольник с такими сторонами существует.")
            self.check_triangle_type()
        else:
            print("Треугольник с такими сторонами не существует.")

    def check_triangle_type(self):
        if self.a == self.b and self.b == self.c:
            print("Треугольник - равносторонний.")
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            print("Треугольник - равнобедренный.")
        else:
            print("Треугольник - разносторонний.")

triangle = Triangle()
triangle.check_triangle()