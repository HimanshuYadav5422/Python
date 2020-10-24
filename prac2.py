'''Consider a showroom of electronic products, where there are various salesmen.Each salesman
is given a commission of 5%, depending on the sales made per month. Incase the sale done
is less than 50000, then the salesman is not given any commission. Write a function to
calculate total sales of a salesman in a month, commission and remarks for the salesman.
Sales done by each salesman per week is to be provided as input. Use tuples/list to store data of
salesmen. Assign remarks according to the following criteria:
Excellent :Sales>=80000
Good :Sales>=60000and<80000
Average :Sales>=40000and<60000
WorkHard :Sales<40000'''
def salesman():
    sw1=float(input("Enter the sale of week 1:"))
    sw2=float(input("Enter the sale of week 2:"))
    sw3=float(input("Enter the sale of week 3:"))
    sw4=float(input("Enter the sale of week 4:"))
    stotal=sw1+sw2+sw3+sw4
    if(stotal>=50000):
        commission=stotal*0.05
    else:
        commission=0
    if(stotal>=80000):
        remark="Excellent"
    elif(stotal>=60000):
        remark="Good"
    elif(stotal>=40000):
        remark="Average"
    else:
        remark="WorkHard"
    sale=[stotal,commission,remark]
    print("Total sales of the month:",sale[0])
    print("Commision:",sale[1])
    print("Remark:",sale[2])
def main():
    salesman()
if __name__ == '__main__':
    main()
