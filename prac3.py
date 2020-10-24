'''Write a Python function to find the nth term of Fibonacci sequence and its
factorial. Return the result as a list.'''
def ft(c):
    fact=1
    for i in range(1,c+1):
        fact*=i
    return fact
def fseries():
    a=int(input("Enter the first term of Fibonacci series:"))
    b=int(input("Enter the second term of Fibonacci series:"))
    n=int(input("Enter which term you to get:"))
    for i in range(0,n-2):
        c=a+b
        a=b
        b=c
    fact=ft(c)
    return [c,fact]

def main():
    list=fseries()
    print("nth term of the Fibonacci series:",list[0])
    print("Factorail of the given no:",list[1])
if __name__ == '__main__':
    main()
