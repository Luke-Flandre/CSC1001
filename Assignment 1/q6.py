from math import sin     #import the maths dunction
from math import cos
from math import tan

func=input('Enter trigonometric function (sin, cos, or tan):')
def ftri(x,func):  #judge which function the user put in
    if func=='sin':#the user put in 'sin',for example
        return sin(x)#the function should be 'sin' as well
    elif func=='cos':
        return cos(x)
    elif func=='tan':
        return tan(x)
    else:    #in case the user input something wrong
        raise ValueError('Invalid function,please enter sin, cos or tan!')
    

try:#  handle invalid condition
    n=int(input('Enter the number of sub-intervals:'))
    a=eval(input('Enter left endpoint of interval:'))
    b=eval(input('Enter right endpoint of interval:'))
except ValueError:#in case the user input invalid n
    print('Invalid number,please enter an integer "n"!')

if a>=b:# handle the condition when left side is greater than right side
    print('a should smaller than b')
else:#proper situation
    sum=0  #calculate the formula
    for i in range(1,n+1):
        x=(b-a)/n*(i-0.5)+a
        f=ftri(x,func)#using the trigonometric functions
        sum+=(b-a)/n*f#sun up each result
    result=sum
    print('The numerical integration of',func,' over [',a,',', b,'] with ',n, ' sub-intervals is:', result)

    
          
