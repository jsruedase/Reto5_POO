from shape_package.shape import Shape

class Rectangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.width = self.get_width()
        self.height = self.get_height()
    
    def get_height(self):
        return self._edges[0].get_length()
    
    def get_width(self):
        return self._edges[1].get_length()  

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return super().compute_perimeter()

class Square(Rectangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.side = self.get_side()
    
    def get_side(self):
        return self.width

    def compute_area(self):
        return self.side**2

    def compute_perimeter(self):
        return super().compute_perimeter()