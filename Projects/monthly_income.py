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
def get_month():
    while True:
        months = 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'
        month = input("Enter the month: ")
        month = month.title()
        if month in months:
            return month
        else:
            print("Invalid month. Please enter a valid month.")
        print(f"The current month is: {month}")        

def job_income():
    jobs = []
    income = []   
    while True:
        job_input = input("Enter the job name (or enter 'q' to finish): ")
        job_input = job_input.title()
        if job_input.lower() == 'q':
            break
        else:
            while True:
                try:
                    income_input = float(input(f"Enter the income for {job_input}: $"))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid numeric income.")
           
            jobs.append(job_input)
            income.append(income_input)
            # counter +=1     
    return jobs, income

def display_jobs(jobs, incomes, month):
    print(f"Here are the income for the month of {month} you have entered: \n")
    for i in range(len(jobs)):
        print(f"{i + 1}. {jobs[i]} : ${incomes[i]:,.2f}\n")
    print(f"The total income for the month is: ${sum(incomes):,.2f}\n")

def write_output_file(selected_month, jobs, income, file_name='monthly income.txt'):
    with open(file_name, 'a') as file:
        file.write(f"Here are the income for the month of {selected_month} you have entered: \n")
        for i in range(len(jobs)):
            file.write(f"{i + 1}. {jobs[i]} : ${income[i]:,.2f}\n")
        file.write(f"The total income for the month is: ${sum(income):,.2f}\n")


# execute the functions below (main execution)
if __name__ == "__main__" :
    selected_month = get_month()
# job_list, income_list = job_income()
    jobs, income = job_income()
# display_jobs(job_list, income_list, month)
    display_jobs(jobs, income ,selected_month)
    write_output_file(selected_month, jobs, income)