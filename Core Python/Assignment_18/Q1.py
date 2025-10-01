class Complex_Number():
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def __del__(self):
        print(f"Destructor called for {self.real} + {self.imag}i")


    def __add__(self,other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex_Number(real,imag)
    def __sub__(self,other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return Complex_Number(real,imag)
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
obj = Complex_Number(4,5)
obj1 = Complex_Number(6,7)
print(obj + obj1)
print(obj - obj1)
        