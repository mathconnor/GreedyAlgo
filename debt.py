"""
Write a program to calculate the credit card balance after one year if a person only pays the
minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance.
At the end of 12 months, print out the remaining balance.
Be sure to print out no more than two decimal digits of accuracy

A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

# def balance_total(balance, annualInterestRate, monthlyPaymentRate):

# balance = 1000
# unpaid = 0
# annualInterestRate = 0.10
# monthlyPaymentRate = 0.1
# monthlyInterestRate = annualInterestRate/12.0
#
# while balance > 0:
#     minimumMonthlyPayment = monthlyPaymentRate * balance
#     format(minimumMonthlyPayment, '2g')
#     print('minimumMonthlyPayment: ', minimumMonthlyPayment)
#     unpaid = balance - minimumMonthlyPayment
#     format(unpaid, '2g')
#     print("unpaid", unpaid)
#     balance = unpaid + (monthlyInterestRate * unpaid)
#     format(balance, '2g')
#     print("balance", balance)

balance = 3329
annualInterestRate = 0.2
monthlyPaymentRate = 0
init_balance = balance
monthlyInterestRate = annualInterestRate/12

while balance > 0:
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > 0:
        print("monthlyPaymentRate" , monthlyPaymentRate)
        monthlyPaymentRate += 10
        balance = init_balance
    elif balance <= 0:
        break
print('Lowest Payment:', monthlyPaymentRate)
