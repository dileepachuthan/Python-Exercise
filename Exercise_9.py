Pretend that you have just opened a new savings account that earns 4 percent interest per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display each amount so that it is rounded to 2 decimal places

r = 4
y = int(input("enter year:"))
if y>3:
    print("Error!")
for i in range(y):

    if y == 1:
        n = int(input("Enter Amount:"))
        p = n*y*r/100
        n = n+p
        print("Principal is:",p)
        print("Savings in 1 year is:{:.2f}".format(n))
        pass
        y = int(input("enter year:"))
    if y == 2:
        p = float(n*y*r/100)
        print("Principal is:",p)
        n = n+p
        print("Savings in 2 years is:{:.2f}".format(n))
        pass
        y = int(input("enter year:"))
    if y == 3:
        p = float(n*y*r/100)
        print("Principal is:",p)
        n = n+p
        print("Savings in 3 years is:{:.2f}".format(n))
