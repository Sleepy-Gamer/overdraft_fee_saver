# overdraft_fee_saver
A short program to save on overdraft fees

This program requires that Python 3 installed.

Please have the program saved in the same folder as the CSV files you are intending to use.

This program is intented to run in the command line.

When running the program please include the name of the CSV file that you would like to use after the program name

Example: **python overdraft_fee_saver.py customer-1234567-ledger.csv**

The following assumptions have been made:
- The program will work with one CSV file at a time
- If the Savings account can reduce how much the Current account has in it's overdraft, it will transfer it, even if this leaves the Current account still in the overdraft.
- The Savings account will only transfer enough to get the Current account out of the overdraft
- Overdraft and interest fees are not to be calculated
-The CSV files will be internal safe files as this is a prototype
-The CSV files will be within the same folder as the prototype program
