#Return true if the card number is valid
def isvalid(number):
    if (sumOfDoubleEvenPlace(number)+sumOfOddPlace(number))%10==0:#valid card number should satisfy step 4
        if len(str(number))>=13 and len(str(number))<=16:#valid card number has 13 to 16 digits
           return True
    return False#all the other card number is invalid
    
#Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    total=0
    numberstr=str(number)#change the number into string touse len() function
    for i in range(0,len(numberstr),2):#choose every secong digit from left to right
        total+=getDigit(int(numberstr[i])*2)#calculate step2, sum of double even place
    return total#return sum of double even place
    
#Return this number if it is a single digit, otherwise, return
#the sum of the two digits
def getDigit(number):
    if number<10:#for single digit
        return number
    
    else:#for twodigit number
        return number//10+number%10#sum up the two digits
        

#Return sum of odd place digits in number
def sumOfOddPlace(number):#the same in sumOfDoubleEvenPlace()
    total=0
    numberstr=str(number)
    for i in range(1,len(numberstr),2):#choose all the digits in odd place
        total+=int(numberstr[i])
    return total
    
numberinput=input('Please enter your credict card number:')
try:
    Numberinput=int(numberinput)#check whether the user input an interger
    if isvalid(numberinput):#that is, if True
            print('Your credict card number is valid!')
    else:#if False
            print('Your credict card number is invalid!')
except ValueError:
    print('Please enter an interger!')

    

    