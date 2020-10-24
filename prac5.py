'''Write a function that finds the sum of the n terms of the following series.
Import the factorial function created in question4.
Series : 1–x2/2!+x4/4!–x6/6!+…xn/n!'''
import prac3
def ssum():
    print("Series:1–x2/2!+x4/4!–x6/6!+…xn/n!")
    n=int(input("Enter the no of terms for which u want to calculate sum:"))
    x=float(input("Enter the value of x:"))
    s=1
    sign=-1
    for i in range(2,2*n):
        fact=prac3.ft(i)
        if (i%2==0):
            s+=((sign*x*i)/fact)
            sign*=-1
    print("The sum of n terms of the series is:",s)
def main():
    ssum()
if __name__ == '__main__':
    main()
