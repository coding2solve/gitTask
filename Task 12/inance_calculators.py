# TASK 12

import math


#Declared variables
deposit = 0
interestRate = 0
investmentYear = 0
compoundInterest = 0
simpleInterest = 0
questionOne = 'simple'

# Selection of user's using the programmeV
selection = input("Select either 'Investment' or 'Bond' from menu below to proceed :" )

#investment selections
if len(selection) == 10 or selection == 'investment':
    print("To calculate amount of interest you'll earn on interest")
    deposit = int(input("Enter amount of money you are depositing: " ))
    interestRate = int(input("Enter Interest rate: " ))
    investmentYear = int(input("How many years do you plan on investing : " ))
    questionOne = input("Do you want simple interest or compound rate Input 'simple' or 'compound' to select rate: ")

    #simple interest
    if questionOne == 'simple':
        simpleInterest = deposit * (1 + interestRate * investmentYear)
        print(f'Your Simple interest rate is : {int(simpleInterest)}')

    #compound interest
    else:
        compoundInterest = deposit * math.pow((1 + interestRate), investmentYear)
        print(f'Your Compound Interest is : {int(compoundInterest)}')

#bond selection
elif selection == 'bond':
    print("To calculate the amount of interest you'll have to pay on a home loan")
    pv = int(input("Enter  present value of the house: " ))
    r = int(input("Enter interest rate: " ))
    n = int(input("How many months to repay bond: " ))

    repayment = pv / (1-(1-((r/100))**n) / r)
    print(f'You are to repay: R {int(repayment)}')







