from TemplateParser import  getNumberslots
from ExtractFeaturesForAlignment import extractNumberVectorFromQuestion, findAlignment

def extractAlignmentFeatures(wordproblem, equationTemplate, solution, templateIndex, type):
    featureVector = []
    correctAlignment = []
    #numberVector = extractNumberVectorFromQuestion(wordproblem)
    noOfNumberSlots = len(getNumberslots(equationTemplate)) 
    if(type == 'train'):
        correctAlignment, numberVector = findAlignment(wordproblem, equationTemplate, solution)
    else:
        numberVector = extractNumberVectorFromQuestion(wordproblem)
    print numberVector
    correctAlignedIndices = []
    if len(correctAlignment) != 0:
        for each in correctAlignment:
            correctAlignedIndices.append(numberVector.index(each))

    

    while len(numberVector) != 10:
        numberVector.append(0)

    featureVector.append(noOfNumberSlots)
    featureVector = featureVector + numberVector + [templateIndex]

    #print (featureVector, correctAlignedIndices)
    return (featureVector, correctAlignedIndices)

