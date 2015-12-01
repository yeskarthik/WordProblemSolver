from AlignmentFeatures import extractAlignmentFeatures
from TemplateParser import solveEquations
from ExtractFeaturesForAlignment import extractNumberVectorFromQuestion
from TemplateParser import solveEquations, getNumberslots
from sympy import Symbol

def testAlignments(test_data,classifier):
    x0 = Symbol('x0')
    featuresets = []
    correctlyAlignedIndicesList = []
    for (i, iIndex, wordproblem, equationTemplate, solution) in test_data:
        alignmentFeatures, correctlyAlignedIndices = extractAlignmentFeatures(wordproblem, equationTemplate, solution, i)        
        featuresets.append(alignmentFeatures)
        alignedString = ''
        for c in correctlyAlignedIndices:
            alignedString += str(c)

        correctlyAlignedIndicesList.append(alignedString)
    prediction = classifier.predict(featuresets)

    predictedAlignedIndices = []
    correct = 0

    for each in prediction:
        item = []
        for char in each:
            item.append(int(char))
        predictedAlignedIndices.append(item)

    #print 'sdsdsdsdsdsdsd'
    #print predictedAlignedIndices
    predictedAlignedValues = []
    for x in range(0, len(test_data)):
        try:
            i, iIndex,wordproblem, equationTemplate, solution = test_data[x]
            numberVector = extractNumberVectorFromQuestion(wordproblem)
            correctAlignValues = []
            for each in predictedAlignedIndices[x]:
                correctAlignValues.append(numberVector[each])
            predictedAlignedValues.append(correctAlignValues)
            #print 'correctalignedvalues'
            #print correctAlignValues
            result = solveEquations(equationTemplate, getNumberslots(equationTemplate), correctAlignValues)
            if solution[0] == result[x0]:
                correct += 1
        except:
            pass
        #print 'all values'
        #print predictedAlignedValues


    #for i in range(0,1):
        #print correctlyAlignedIndicesList[i], prediction[i]
    #    if correctlyAlignedIndicesList[i] == prediction[i]:
    #        correct += 1
    #print 'Correct: ' + str(correct)
    accuracy = (correct/float(len(test_data)))
    return accuracy


