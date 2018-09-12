#Assignment-5
#w.a.p to create a triangle and find perimeter and area of that triangle

import math
class triangle:
    def __init__(self,side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def perimeter(self):
        p = self.side1+self.side2+self.side3
        print("Perimeter is",p)
    def area(self):
        s = (self.side1+self.side2+self.side3)/2
        a = math.sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3))
        print("Area is",a)


#test case
t1 = triangle(3,4,5)
t1.perimeter()
t1.area()
