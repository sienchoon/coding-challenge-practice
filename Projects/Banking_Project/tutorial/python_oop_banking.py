# https://www.youtube.com/watch?v=PMFd95RgIwE&ab_channel=DaveGray
# banking app tutorial 
# create a user account
# create password and user login information
# deposit
# withdraw
# check balance
# statement

class BankAccount:
    def __init__(self, accountName, accountBalance):
        self.name = accountName
        self.balance = accountBalance
        print(f"Bank Account Name: {self.name} | Balance: ${self.balance:.2F}")