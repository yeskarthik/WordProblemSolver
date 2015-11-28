import re
#from ExtractFeaturesForAlignment import extractNumberVectorFromQuestion

def getNumberslots(template):
    numbers = []
    for eq in template:
        m = re.findall('(?<=n)\d+', eq)
        numbers = numbers + m
    for i in range(0, len(numbers)):
        numbers[i] = 'n'+numbers[i]
    
    #print numbers
    numbers = list(set(numbers))
    return numbers


from sympy.solvers import solve
from sympy import Symbol

def solveEquations(equations, numberSlots, alignedNumbers):
    x0 = Symbol('x0')
    x1 = Symbol('x1')
    #sanitize equation
    sanitized = []
    for eq in equations:
        g = eq.split('=')
        g[1] = g[1].replace('+', '$').replace('-', '+').replace('$', '-')
        eq = g[0] + '-' + g[1]
        #print eq
        for i in range(0, len(numberSlots)):
            eq = eq.replace(numberSlots[i], str(alignedNumbers[i]))
        sanitized.append(eq)

    #print sanitized
    if len(sanitized) == 1:
        result = solve((sanitized[0]), x0)
        #print sanitized
        #print result
        if(len(result)>=1):
            result = {x0: result[0]}
    elif len(sanitized) == 2:
        result = solve((sanitized[0], sanitized[1]), x0, x1)
    #print 'result: ', result
    return result


#equation = [u'n0+(n1*x0)=n2+(n3*x0)']

#alignedNumbers = extractNumberVectorFromQuestion('A writing workshop enrolls novelists and poets in a ratio of 5 to 3. There are 24 people at the workshop. How many novelists are there? How many poets are there?')
#alignedNumbers = [22.0, 0.13, 8, 0.18, 2.0, 2.0]
#alignedNumbers = find
#print getNumberslots(equation)
#solveEquations(equation, getNumberslots(equation), alignedNumbers)
