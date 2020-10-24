'''Write a menu driven program to perform the following on strings:
a)Find the length of string.
b)Return maximum of three strings.
c)Accept a string and replace all vowels with “#”
d)Find number of words in the given string.
e)Check whether the string is a palindrome or not.'''
def main():
    a='y'
    while a=='y':
        n=int(input("Press 1:Find the length of string\nPress 2:Return maximum of three strings.\
        \nPress 3:Accept a string and replace all vowels with hash\
        \nPress 4:Find number of words in the given string.\nPress 5:Check whether the string is a palindrome or not.\n "))
        if(n==1):
            str=input("Enter a string of which u want to calculate length:")
            count=0
            for i in str:
                count+=1
            print("length of string:",count)
        elif(n==2):
            str1=input("Enter string 1:")
            str2=input("Enter string 2:")
            str3=input("Enter string 3:")
            print("Greatest string:")
            if(str1>=str2):
                if(str1>str3):
                    print(str3)
                else:
                    print(str1)
            elif(str1<str2):
                if(str2>str3):
                    print(str2)
                else:
                    print(str3)

        elif(n==3):
            str=input("Enter a string:")
            print("Updated string:")
            for i in str:
                if((i=='a')or(i=='e')or(i=='i')or(i=='o')or(i=='e')):
                    i='#'
                print(i,end="")
        elif(n==4):
            count=1
            str=input("Enter a string:")
            for i in str:
                if(i==' '):
                    count+=1
            print("No of words in string:",count)
        elif(n==5):
            str=input("Enter a string:")
            j=len(str)-1
            for i in range(0,int(len(str)/2)):
                if(str[i]!=str[j]):
                    print("String is not palindrome.")
                    break
                i+=1
                j-=1
            else:
                print("String is palindrome.")
        a=input("\nPress y to continue:")
if __name__ == "__main__":
    main()
