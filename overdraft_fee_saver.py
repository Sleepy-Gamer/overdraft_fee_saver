#!/usr/bin/python3
#Backbase Tech Test
#Katherine Axten

from datetime import datetime
import csv
import sys


#Add in so that you can list which file ot be used in the command line
filename = sys.argv[1]
print("This is the file name you have checked:", filename)
#This will take the last argument of the command line as the file name

#In the assumptions it is noted that balances start at 0
current_account_balance = ""
savings_account_balance = ""
current_account_number = ""
savings_account_number = ""
amount_to_transfer = 0.0
#Get todays date and the current time
today = datetime.now()
today_string = today.strftime("%Y-%d-%mT%H:%M:%S")


#Open the CSV file that has been specified.
with open(filename) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ',')
    for entry in csv_reader:
        if (entry['AccountType'] == 'CURRENT'):
            #Puts the last current account entry into the variable as a STRING
            current_account_balance = entry['TransactionValue']
            current_account_number = entry['AccountID']

        if(entry['AccountType'] == 'SAVINGS'):
            savings_account_balance = entry['TransactionValue']
            savings_account_number = entry['AccountID']
            

    #Convert the values to floats
    current_account_balance = float(current_account_balance)
    savings_account_balance = float(savings_account_balance)

    print("The Current Account balance is:", current_account_balance)
    print("The Savings Account balance is:", savings_account_balance)

    #Do the math to check the values of the current account
    if(current_account_balance < 0):
        print("The Current Account is in the overdraft")
        #Check the balance of the savings account
        if(savings_account_balance > 0):
            print("There is money in the Savings Account which can be transfered")
            #if the balance is greater than 0 then money can be transfered to the current account.
            if(savings_account_balance >= -current_account_balance):
                #If there is more money in the savings account then we only want to transfer enought to get out of the overdraft
                amount_to_transfer = -current_account_balance
                print("The amount to be transfered is:", amount_to_transfer)
            elif (savings_account_balance < -current_account_balance):
                #If there is money in the savings account but it won't cover all of it, then transfer it to reduce costs. 
                amount_to_transfer = savings_account_balance
                print("The amount to be transfered is:", amount_to_transfer)
        else:
            #The savings account balance is 0
            print("Unfortunately there are insufficient funds in the savings account at this time")
            amount_to_transfer = 0.0

        #Round to 2 decimal places to make it more "bank balance"
        new_current_account_balance = round(current_account_balance + amount_to_transfer, 2)
        new_savings_account_balance = round(savings_account_balance - amount_to_transfer, 2)

        #This writes in a new entry if a change has been made.
        if(amount_to_transfer > 0.0):
            with open(filename, 'a') as csv_file:
                ledger_writer = csv.writer(csv_file, delimiter = ',')
                to_write = [savings_account_number, 'SAVINGS', 'SYSTEM', today_string, new_savings_account_balance]                
                ledger_writer.writerow(to_write)
                to_write = [current_account_number, 'CURRENT', 'SYSTEM', today_string, new_current_account_balance]
                ledger_writer.writerow(to_write)

    else:
        print("Current account is not in the overdraft")
    