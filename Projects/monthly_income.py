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
def month():
    month = input("Enter the month: ")
    month = month.title()
    return f"The current month is: {month}"

month() 

def job_income():
    jobs = []
    income = []
    counter = 0
    
    while True:
        job_input = input("Enter the job name (or enter 'q' to finish): ")
        job_input = job_input.title()
        if job_input.lower() == 'q':
            break
        else:
            jobs.append(job_input)
            counter +=1 
            
    print("Here are list of jobs you have entered: \n")
    counter = 1
    for job in jobs:
        print(f"{counter}. {job}")
        counter += 1

job_income()

    

