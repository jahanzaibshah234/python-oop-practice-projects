#User function Template for python3
#Complete the given class
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    # Overload the + operator for adding two complex numbers
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    # Overload the string representation of the object
    def __str__(self):
        # Your code here
        return f"{self.real} + {self.imaginary}i"