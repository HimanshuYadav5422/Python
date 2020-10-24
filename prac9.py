'''Use dictionary to store marks of the students in 4 subjects. Write a function to
find the name of the student securing highest percentage.(Hint:Names of
students are unique).'''
def hp(stu):
    max=0
    for i in stu:
        if(max<sum(stu[i])/4):
            max=sum(stu[i])/4
    for i in stu:
        if(max==sum(stu[i])/4):
            print("Name of student scoring highest marks:",i)
    
def main():
    stu={"Himanshu":[98,95,95,95],"Anil":[98,95,95,80],"Sunil":[93,83,95,90]}
    hp(stu)
if __name__ == "__main__":
    main()