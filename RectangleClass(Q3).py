# Write a python program to create a class ‗Rectangle‘. This class should include a
# constructor to initialize the dimensions. Include a function in the class to compute the area of
# the rectangle. Create objects of the class and print area.

#Class defination
class reactangle:
    def __init__(self,len,bre):
        self.l=len
        self.b=bre
    def area(self):
        print("area is ",self.l*self.b)
r=reactangle(3,14)
r.area()        