'''Write a function that takes a number(>=10) as an input and return the digits of the
number as a set.'''
def digit():
    n=int(input("Enter a number:"))
    assert n>=10
    nset=set() 
    while n>0:
        r=n%10
        n=int(n/10)
        nset.add(r)
    return nset
def main():
    ns=set()
    ns=digit()
    print("Digits in the number:",ns)
if __name__ == '__main__':
    main()
