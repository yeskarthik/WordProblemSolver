from TemplateParser import  getNumberslots
from ExtractFeaturesForAlignment import extractNumberVectorFromQuestion, findAlignment, findNumberFeatures

def extractAlignmentFeatures(wordproblem, equationTemplate, solution, templateIndex, type):
    featureVector = []
    correctAlignment = []
    #numberVector = extractNumberVectorFromQuestion(wordproblem)
    noOfNumberSlots = len(getNumberslots(equationTemplate)) 
    if(type == 'train'):
        correctAlignment, numberVector = findAlignment(wordproblem, equationTemplate, solution)
    else:
        numberVector = extractNumberVectorFromQuestion(wordproblem)
    #print numberVector
    correctAlignedIndices = []
    if len(correctAlignment) != 0:
        for each in correctAlignment:
            correctAlignedIndices.append(numberVector.index(each))    

    while len(numberVector) != 10:
        numberVector.append(0)

    

    #featureVector.append(noOfNumberSlots)
    #featureVector = featureVector + numberVector + [templateIndex]
    featureVector = findFeatures(equationTemplate, wordproblem) 

    #print (featureVector, correctAlignedIndices)
    return (featureVector, correctAlignedIndices)


def findFeatures(equationTemplate, wordproblem):

    featureVector = None
    numberFeatures = findNumberFeatures(wordproblem)        
    while len(numberFeatures) != 10:
        numberFeatures.append(-1)
    featureVector = numberFeatures

    if str(equationTemplate) == "[u'(n0*x0)+(n1*x1)=n2', u'x0+x1=n3']":
        print equationTemplate
    else:
        print equationTemplate
    
    return featureVector
