#Project Title:  Monthly income calculator

#how many income from jobs, frequency (weekly/fortnightly/monthly)
#gross income vs income after tax
#tax rate
#date of payment
#export as csv/.txt file



def income():
    income = input("Enter the amount of income: $")
    job = input("Which job did you get income from: ").title()
    paydate = input("Enter the date of payment(DD/MM/YYYY): ")
    print(f'Your income from {job} is ${income} and was paid on {paydate}')





