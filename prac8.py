'''Write a Python program to perform the following using list:
a) Check if all elements in list are numbers or not.
b) If it is a numeric list,then count number of odd values in it.
c) If list contains all Strings,then display largest String in the list.
d) Display list in reverse form.
e) Find a specified element in list.
f) Remove the specified element from the list.
g) Sort the list in descending order.
h) Accept 2 lists and find the common members in them.'''

def main():
    a='y'
    while a=='y':
        n=int(input("Press 1 to check if all elements in list are numbers or not.\
        \nPress 2 to check if it is a numeric list,then count number of odd values in it.\
        \nPress 3 to check if list contains all Strings,then display largest String in the list.\
        \nPress 4 to display list in reverse form.\
        \nPress 5 to find a specified element in list.\
        \nPress 6 to remove the specified element from the list.\
        \nPress 7 to sort the list in descending order.\
        \nPress 8 to accept 2 lists and find the common members in them."))
        if(n==1):
            l=[1,3,7,26,50,'car']
            for i in l:
                if(type(i)!=int):
                    print("This list contains some strings.")
                    break
            else:
                print("This list contains numeral only")
        elif(n==2):
            l=[1,3,7,26,50]
            for i in l:
                if(type(i)!=int):
                    print("This list contains some strings.")
                    break
            else:
                count=0
                for i in l:
                    if(i%2!=0):
                        count+=1
                print("No of odd values in list:",count)
        elif(n==3):
            l=['car','himanshu']
            for i in l:
                if(type(i)==int):
                    print("This list contains some numerals.")
                    break
            else:
                for i in l:
                    for j in l:
                        if(i<j):
                            break
                        elif(i==j):
                            continue
                    else:
                        print("Greatest string:",i)
                        break
        elif(n==4):
            l=[1,3,5,'Akash']
            count=0
            for i in l:
                count+=1
            count-=1
            print("List in reverse order:",end='')
            while count>=0:
                print(l[count],end=' ')
                count-=1
            print()
        elif(n==5):
            q=input("Enter the element to be searched")
            if(q.isnumeric()==True):
                q=int(q)
            l=[1,3,5,'Akashi']
            for i in l:
                if(i==q):
                    print("Element is present in the list.")
                    break
            else:
                print("Element not found in the list.")
        elif(n==6):
            l=[1,3,5,'Akash']
            q=input("Enter the element to be removed")
            if(q.isnumeric()==True):
                q=int(q)
            for i in l:
                if(q==i):
                    l.remove(q)
                    break
            else:
                print("This element is not present in the list.")
            print("List:",l)
        elif(n==7):
            l=[1,3,5,7,100,81]
            l.sort()
            l.reverse()
            print("List:",l)
        elif(n==8):
            l1=[]
            l2=[]
            q1=int(input("Enter the no of value u want to enter in list1:"))
            for i in range(1,q1+1):
                d=input(f"Enter the {i}th element of list 1:")
                if(d.isnumeric()==True):
                    d=int(d)
                l1.append(d)
            q2=int(input("Enter the no of value u want to enter in list2:"))
            for i in range(1,q2+1):
                d=input(f"Enter the {i}th element of list 2:")
                if(d.isnumeric()==True):
                    d=int(d)
                l2.append(d)
            print("List1:",l1)
            print("List2:",l2)
            print("Common element:",end="")
            for i in l1:
                for j in l2:
                    if(i==j):
                        print(i,end="    ")
            print()
        else:
            print("Wrong choice.")
        a=input("Press y to continue:")
if __name__ == "__main__":
    main()