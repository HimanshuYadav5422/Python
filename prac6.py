'''Consider a tuple t1={1,2,5,7,9,2,4,6,8,10}. Write a program to perform following
operations:
a)Print another tuple whose values are even numbers in the given tuple.
b)Concatenate a tuplet2={11,13,15) with t1.
c)Return maximum and minimum value from this tuple.'''
def main():
    t1=(1,2,5,7,9,2,4,6,8,10)
    t=[]
    max,min=t1[0],t1[0]
    for i in t1:
        if(i%2==0):
            t.append(i)
        if(max<i):
            max=i
        if(min>i):
            min=i
    t=tuple(t)
    print("Tuple:",t)
    t2=(11,13,15)
    t1=t1+t2
    print("Tuple 1 after concatenation:",t1)
    print("Maximum value in tuple:",max)
    print("Minimum value in tuple:",min)
if __name__ == "__main__":
    main()