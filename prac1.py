'''Write a function that takes the lengths of three sides:side1, side2 and side3 of the triangle
as the input from the user using input function and return the area and perimeter of the triangle
as a tuple. Also, assert that sum of the length of any two sides is greater than the third side.'''
import math
def trianglearea ():
    side1=float(input("Enter the first side of triangle:"))
    side2=float(input("Enter the second side of triangle:"))
    side3=float(input("Enter the third side of triangle:"))
    assert (side1+side2>=side3)or(side1+side3>=side2)or(side2+side3>=side1)
    speri=(side1+side2+side3)/2
    area=math.sqrt(speri*(speri-side1)*(speri-side2)*(speri-side3))
    return area,2*speri
def main():
    area,peri=trianglearea()
    print("Area of the triangle:",area)
    print("Perimeter of the triangle:",peri)
if __name__ == '__main__':
    main()
