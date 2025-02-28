finalAccountValue=eval(input('Enter the final account value:'))#input final account value
annualInterestRate=eval(input('Enter the annual interest rate:'))#input annual interest rate
numberOfYears=eval(input('Enter the number of years:'))#input number of years
initialDepositAmount=finalAccountValue/(1+annualInterestRate/100)**numberOfYears#calculate the initial amount of money
print('The initial value is:',initialDepositAmount)#print out the outcome
