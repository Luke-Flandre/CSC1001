def isprime(n):#define a fuction that jugde whether a number is prime number
    if n<2:
        return False#if a number is negative or 0 or 1, it is not a prime number
    for i in range(2,n):
        if n%i==0:
            return False#if a number is divisible by ant number except 1 and itself, it is not a prime number
    return True#the number left is prime number

def isemirp(n):#define a fuction that jugde whether a number is emirp number
    if isprime(n):#the number should be prime number first
       reversen= int(str(n)[::-1])#make the number spell backward
       return reversen!=n and isprime(reversen)#cross out palindromics and not rmirp numbers, only both the statment is true can it return true
    return False#the number else is not what we want

count=0 
number=13#set the original count number and the number we begin with
while count<100:#start a loop
    if isemirp(number):#is a number is emirp
       if number//10<10:#to let the output right aligned
          print(' '*5,number,end='')
       elif number//10<100:
           print(' '*4,number,end='')
       else:
           print(' '*3,number,end='')
        
       count+=1#update the count
       if count%10==0:
             print('')#move to another line when the original line has 10 integer
    number+=1#move to the next number
        


        
    
        