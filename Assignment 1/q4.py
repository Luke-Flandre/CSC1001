n = int(input('Enter a positive integer: '))
if n <= 0:
    print('Must input a positive integer') #In case the user input an invalid number
else:
    print('m','m+1','m**(m+1)',sep='\t') #print the table
    for m in range(1, n+1):
     mm1 = m * m + 1  # calculate mm+1
     print(m, m+1, mm1, sep='\t') #print the content of the table
 
