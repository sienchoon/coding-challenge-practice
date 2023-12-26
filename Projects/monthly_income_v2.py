# Import libraries
import time 

# Create empty list
INCOME = []
DATES = []
JOB =[]

# Function to add the incomes, dates and jobs to the lists to organise the data
def add_income(income, date, job):
    INCOME.append(income)
    DATES.append(date)
    JOB.append(job)
    
#main program, user input selection
def main():
    option = -1
    while option != 0:
        print("Welcome to Income Tracker")
        print("Enter 1 to Add income")
        print("Enter 2 to Display income")
        print("Enter 3 to Save Income Report")
        print("Enter 0 to Exit")
        option = int(input("Enter your choice: "))
        time.sleep(0.5)
        
        if option == 0:
            print("Thank you for using the program. Goodbye!")
        elif option == 1:
            income = float(input("Enter income: $ "))
            date = input("Enter date in this format DD/MM/YYYY: ")
            job = input("Enter job: ")
            time.sleep(1)
            add_income(income, date, job)

        elif option == 2:
            print("Income:")
            for i in range(len(INCOME)):
                print(f"{i+1}. ${INCOME[i]} on {DATES[i]} for {JOB[i]}")
                time.sleep(1)
                
        elif option == 3:
            income_df = pd.DataFrame(list(zip(INCOME, DATES, JOB)), columns = ["Income", "Date", "Job"])
            income_df.to_csv("income.csv", index = False)
            print("Income report saved to income.xlsx")
            print(income_df)
            
        else:
            print("Invalid option, please select the options 0, 1, 2, or 3.")
            
main()