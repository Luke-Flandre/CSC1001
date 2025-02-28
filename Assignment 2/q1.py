def sqrt(n):
    if n==0:
        return n
    elif n<0:
        print('Please enter a non-negative number!')
    else:
        last_guess = 1# Set the initial guess to 1
        difference = 0.0001# Set the maximum difference between guesses
        # loop until the difference between guesses is less than difference
        while True:
            next_guess = (last_guess + (n / last_guess)) / 2# Calculate the next guess
            if abs(next_guess - last_guess) < difference:# Check if the difference between guesses is less than epsilon   
                return next_guess# Return the next guess as the square root of n
            last_guess = next_guess# Set the next guess as the last guess and repeat
            
a=input('Please enter a non-negative number:')
try:
    b=float(a)
    c=sqrt(b)
    if c!= None:
        print('The square root of the number you enter is',c)
except ValueError:
    print('Please enter a non-negative number!')