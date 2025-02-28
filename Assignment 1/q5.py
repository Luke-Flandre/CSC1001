def primenum(num):#definition of the function of judging prime numbers
    if num <= 1:#prime number should be greater than 1
        return False
    for i in range(2, num):
        if num % i == 0:
            return False  #cross out the number which are not prime by the definition of prime number
    else:
        return True#the remaining numbers are prime numbers

try:  #to deal with the invalid condition
    n = int(input("Enter an integer N: "))
    count = 0  #count how many prime numbers
    for i in range(2, n):
        if primenum(i):
            print(i, end=" ")#output the result and than space between the results
            count += 1   #plus the new prime number into count
            if count % 8 == 0:#when a line has 8 results
                print()  #turn to a new line
    if count == 0:
        print("There are no prime numbers smaller than", n) #if therer is no prime number
except :#invalid condition
    print("Invalid error!") 
