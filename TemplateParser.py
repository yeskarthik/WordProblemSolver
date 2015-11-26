import re
from ExtractFeaturesForAlignment import extractNumberVectorFromQuestion

def getNumberslots(template):
    numbers = []
    for eq in template:
        m = re.findall('(?<=n)\d+', eq)
        numbers = numbers + m
    for i in range(0, len(numbers)):
        numbers[i] = 'n'+numbers[i]
    
    #print numbers
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
        eq = g[0]+'-'+g[1]
        for i in range(0, len(numberSlots)):
            eq = eq.replace(numberSlots[i], str(alignedNumbers[i]))
        sanitized.append(eq)

    print sanitized
    result = solve((sanitized[0], sanitized[1]), x0, x1)
    print result


equation = [u'(n0*x0)=(n1*x1)', u'x0+x1=n2']

alignedNumbers = extractNumberVectorFromQuestion('A writing workshop enrolls novelists and poets in a ratio of 5 to 3. There are 24 people at the workshop. How many novelists are there? How many poets are there?')

solveEquations(equation, getNumberslots(equation), alignedNumbers)
