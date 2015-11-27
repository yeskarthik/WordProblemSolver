from AlignmentFeatures import extractAlignmentFeatures

def testAlignments(test_data,classifier):
    featuresets = []
    correctlyAlignedIndicesList = []
    for (i, iIndex, wordproblem, equationTemplate, solution) in test_data:
        alignmentFeatures, correctlyAlignedIndices = extractAlignmentFeatures(wordproblem, equationTemplate, solution, i, 'train')
        featuresets.append(alignmentFeatures)
        alignedString = ''
        for c in correctlyAlignedIndices:
            alignedString += str(c)

        correctlyAlignedIndicesList.append(alignedString)
    prediction = classifier.predict(featuresets)


    correct = 0
    for i in range(0,50):
        #print correctlyAlignedIndicesList[i], prediction[i]
        if correctlyAlignedIndicesList[i] == prediction[i]:
            correct += 1
    print 'Correct: ' + str(correct)


