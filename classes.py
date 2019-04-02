class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name, self.age)

# myclass = MyClass('Praneet', 21)
# myclass.display()

class Complex:
    def __init__(self, real_num, imaginary_num):
        self.real_num = real_num
        self.imaginary_num = imaginary_num

    def display(self):
        print('Real Number:', self.real_num)
        print('Imaginary Number:', self.imaginary_num)
    
    def show_magnitude(self):
        magnitude = self.real_num ** 2 + self.imaginary_num ** 2 
        print('Magnitude:', round(magnitude, 2))
        
comlex = Complex(1.2, 2.5)
comlex.display()
comlex.show_magnitude()
    