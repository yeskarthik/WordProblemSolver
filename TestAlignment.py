from AlignmentFeatures import extractAlignmentFeatures
from TemplateParser import solveEquations
from ExtractFeaturesForAlignment import extractNumberVectorFromQuestion
from TemplateParser import solveEquations, getNumberslots, solveMNEquations
from FeatureReader import readAndConvertFeatures 
from sympy import Symbol

def testAlignments(test_data, classifiers):
    x0 = Symbol('x0')
    featuresets = []
    correctlyAlignedIndicesList = []
    for (i, iIndex, wordproblem, equationTemplate, solution) in test_data:
        try:
            classifier = classifiers[str(equationTemplate)]
        except KeyError:
            continue
        alignmentFeatures, correctlyAlignedIndices = extractAlignmentFeatures(wordproblem, equationTemplate, solution, i, 'train')        
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


    for i in range(0,len(prediction)):
        print correctlyAlignedIndicesList[i], prediction[i]
        if correctlyAlignedIndicesList[i] == prediction[i]:
            correct += 1
    print 'Correct: ' + str(correct)

def testAlignmentPrediction(classifier, test_data):
    featuresets = []
    classes = []
    correct = 0
    equations = []
    m = Symbol('m')
    for (i, iIndex, wordproblem, equationTemplate, solution) in test_data:
        result = readAndConvertFeatures(iIndex)        
        for each in result:
            featuresets.append(each[1])
            classes.append(each[0])
            equations.append(each[2])
        for i in range(0,len(featuresets)):
            predictedclass = classifier.predict(feature)
            if int(predictedclass) == 1:
                equation = equations[i]
                result = solveMNEquations(equations)
                if result[m] == solution[0]:
                    correct += 1
                    break
    print correct


