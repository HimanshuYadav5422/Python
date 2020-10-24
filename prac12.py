'''Write a program that makes use of a function to accept a list of n integers
and displays a histogram.'''
import matplotlib.pyplot as plt
def hgraph():
    l=[]
    n=int(input("Enter the no of intgers u want to enter:"))
    for i in range(0,n):
        l.append(int(input(f"Enter the {i+1} element of list:")))
    print("List of numbers:",l)
    plt.hist(l)
    plt.title("Marks line chart")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()
def main():
    hgraph()
if __name__ == "__main__":
    main()