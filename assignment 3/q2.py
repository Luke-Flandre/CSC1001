class Polynomial:
    def __init__(self, polynomial):# Initialize the polynomial
        self.polynomial = polynomial
    
    def derivative(self):
            terms = self.polynomial.split('+')# Get each term of the polynomial
            derivativeterms = []
            for term in terms:
                term=term.strip('()')# Strip the blank of the term to make sure the program work
                if '*' in term: #Other case include, the constant of the polynomial and the sigle variable
                    coefficient, variable = term.split('*')
                    coefficient = int(coefficient)
                    if '^' in variable:# if it is not a one-time term
                        try:
                            degree = int(variable.split('^')[-1])
                            if degree <0:
                                print('The degree must be a non-negative integer!')
                                return ValueError
                            else:    # Caluculate its derivative
                                derivativedegree = degree - 1
                                if derivativedegree != 1 and derivativedegree != 0:
                                    derivativeterms.append(str(coefficient * degree) + '*' + variable.split('^')[0] +'^' + str(derivativedegree))
                                elif derivativedegree ==1:# No need to return '^' in this case
                                    derivativeterms.append(str(coefficient * degree) + '*' + variable.split('^')[0])
                        except ValueError:
                            print('The degree must be a non-negative integer!')
                            return ValueError
                    else:
                        derivativeterms.append(str(coefficient))# In this case, it is a one-time term,whose ferivative is it's coefficiency
             
                elif term not in ['1','2','3','4','5','6','7','8','9','0'] and len(term) == 1: # If it is not 1,2,3... or something longer, it is a single variable, whose derivative is 1
                    derivativeterms.append('1')
                elif '^' in term:# In case it is the form of 'x^n'
                    degree = int(term.split('^')[-1])
                    variable = term.split('^')[0]
                    if degree <0:
                        print('The degree must be a non-negative integer!')
                        return ValueError
                    else:    
                        derivativedegree = degree - 1
                        if derivativedegree != 1 and derivativedegree != 0:
                            derivativeterms.append(str(degree) + '*' + variable.split('^')[0] +'^' + str(derivativedegree))
                        elif derivativedegree ==1:
                            derivativeterms.append(str(degree) + '*' + variable.split('^')[0])
            result= '+'.join(derivativeterms)# Join the result into a new polynomial
            return result




'''
def samedegree(poly):
        terms = poly.split('+')
        degrees = []
        for term in terms:
            term = term.strip()
            if '*' in term:
                variable = term.split('*')[1]
                if '^' in variable:
                    degree = int(variable.split('^')[1])
                    if degree not in degrees:
                        degrees.append(degree)
                else:
                    if 1 not in degrees:  # If no exponent is provided, the degree is 1
                        degrees.append(1)
            else:
                if 0 not in degrees:  # If no variable is present, the degree is 0
                    degrees.append(0)
        if len(degrees) == 1:
            return True
    


try:
    polynomial = input('Please Enter a Polynomial (the degree should be a non-negative number and coefficient should be put before the variable, and the terms should be different): ')
    
    if samedegree(polynomial):
        print('The terms of thepolynomials should have different degrees!')
    else:
        poly = Polynomial(polynomial)
        result = poly.derivative()
        print("The derivative of the polynomial is:", result)
except ValueError:
    print('Please check the polynomial you entered!')
'''