import math 
from shape_package.shape import Shape

class Triangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.base = self.get_base()
        self.height = self.get_height()
    
    def get_base(self):
        return self._edges[0].get_length()
    
    def get_height(self):
        return 2 * self.compute_area() / self.base

    def compute_area(self):
        return super().compute_area()

    def compute_perimeter(self):
        return super().compute_perimeter()

class Scalene(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.side1 = self.get_side1()
        self.side2 = self.get_side2()
        self.side3 = self.get_side3()
    
    def get_side1(self):
        return self._edges[0].get_length()
    
    def get_side2(self):
        return self._edges[1].get_length()
    
    def get_side3(self):
        return self._edges[2].get_length()

    def compute_area(self):
        s = self.compute_perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def compute_perimeter(self):
        return super().compute_perimeter()

class Isosceles(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.base = self.get_base()
        self.side = self.get_side()
    
    def get_base(self):
        return self._edges[0].get_length()
    
    def get_side(self):
        return self._edges[1].get_length()

    def compute_area(self):
        return (self.base * self.height) / 2

    def compute_perimeter(self):
        return super().compute_perimeter()

class Equilateral(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.side = self.get_side()
    
    def get_side(self):
        return self._edges[0].get_length()

    def compute_area(self):
        return (math.sqrt(3) / 4) * self.side**2

    def compute_perimeter(self):
        return super().compute_perimeter()