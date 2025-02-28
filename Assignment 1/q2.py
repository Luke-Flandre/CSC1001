num=(input('Enter an integer:'))
length=len(str(num))-1 #the length of the number (number of digits)
num=eval(num)#turn the number into the form of integer
while num>0:#condition
  a=num//(10**length)#find the first figure of the number
  print(a)
  num=num%(10**length)#cross out the first figure
  length=length-1#move on to the next number of digits

