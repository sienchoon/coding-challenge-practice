#Project Title:  Monthly income calculator

#how many income from jobs, frequency (weekly/fortnightly/monthly)
#gross income vs income after tax
#tax rate
#date of payment
#export as csv/.txt file

# def income():
#     income = input("Enter the amount of income: $")
#     job = input("Which job did you get income from: ").title()
#     paydate = input("Enter the date of payment(DD/MM/YYYY): ")
#     print(f'Your income from {job} is ${income} and was paid on {paydate}')
def month(month):
    month = input("Enter the month: ")
    month = month.title()
    print(f"The current month is: {month}")
month(month) 
def job_income():
    jobs = []
    income = []   
    while True:
        job_input = input("Enter the job name (or enter 'q' to finish): ")
        job_input = job_input.title()
        if job_input.lower() == 'q':
            break
        else:
            try:
                income_input = float(input(f"Enter the income for {job_input}: $"))
            except ValueError:
                print("Invalid input. Please enter a valid numeric income.")
            
            jobs.append(job_input)
            income.append(income_input)
            # counter +=1 
     
    return jobs, income

def display_jobs(jobs, incomes):
    print("Here are the income for the jobs you have entered: \n")
    for i in range(len(jobs)):
        print(f"{i + 1}. {jobs[i]} : ${incomes[i]:,.2f}\n")


job_list, income_list = job_income()
display_jobs(job_list, income_list)


    

