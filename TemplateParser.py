import re

def getNumberslots(template):
    numbers = []
    for eq in template:
        m = re.findall('(?<=n)\d+', eq)
        numbers = numbers + m
    for i in range(0, len(numbers)):
        numbers[i] = 'n'+numbers[i]
    
    #print numbers
    return numbers

parseTemplate([u'(n0*x0)+(n1*x1)=n2', u'x0+x1=n3'])

