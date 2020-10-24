'''Write a menu-driven program to accept a list of student names and perform the following
a. Search an element using linearsearch/binarysearch.
b. Sort the elements using bubblesort/insertionsort/selectionsort.'''
def main():
    l=[]
    n=int(input("Enter the no of student:"))
    for i in range(0,n):
        l.append(input(f"Enter the {i}th element of list:"))
    print("List:",l)

    c=int(input("Press 1 to search an element using linearsearch.\
    \nPress 2 to sort the elements using bubblesort."))
    if(c==1):
        s=input("Enter the name of student u want to search:")
        for i in l:
            if(i==s):
                print(i," is present in the list.")
                break
        else:
            print(s," is not present in the list.")
    elif(c==2):
        for i in range(0,n-1):
            for j in range(0,n-1-i):
                if(l[j]>l[j+1]):
                    t=l[j]
                    l[j]=l[j+1]
                    l[j+1]=t
        print("Updated list:",l)
if __name__ == "__main__":
    main()