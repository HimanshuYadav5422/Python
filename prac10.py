'''Write a function that takes a sentence as input from the user and calculates
the frequency of each letter. Use a variable of dictionary type to maintain the
count.'''
def cnt():
    st=input("Enter a sentence:")
    s={}
    for i in st:
        if(i==' ')or(i=='.'):
            continue
        count=0
        for j in st:
            if(i==j):
                count+=1
        s.update({i:count})
    print("Frequency of each letter in sentence\n",s)
def main():
    cnt()
if __name__ == "__main__":
    main()