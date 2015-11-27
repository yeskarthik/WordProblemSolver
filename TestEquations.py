from FeatureExtractor import extractFeatures, numberOfNumbers, numberOfQuestions, numberOfPercent
from sklearn import metrics
import numpy

def testScikitEquations(classifier, vectorizer, labeled_data):

    wordproblems = []
    onlyIndices = []
    for (i, iIndex, wordproblem, equationTemplate, solution) in labeled_data:
        wordproblems.append(wordproblem)
        onlyIndices.append(i)
    test_featuresets = vectorizer.transform(wordproblems).toarray()

    numofnums = []
    numofques = []
    numofpercent = []
    for i in range(0, len(test_featuresets)):
        nums = numberOfNumbers(None, wordproblems[i])
        numofnums.append(nums)
        ques = numberOfQuestions(wordproblems[i])
        numofques.append(ques)
        perc = numberOfPercent(wordproblems[i])
        numofpercent.append(perc)

    numofnums = numpy.array(numofnums)
    numofques = numpy.array(numofques)
    numofpercent = numpy.array(numofpercent)

    test_featuresets = numpy.hstack((test_featuresets, numpy.atleast_2d(numofnums).T))
    test_featuresets = numpy.hstack((test_featuresets, numpy.atleast_2d(numofques).T))
    test_featuresets = numpy.hstack((test_featuresets, numpy.atleast_2d(numofpercent).T))

    #print test_featuresets
    prediction = classifier.predict(test_featuresets)
    score = metrics.accuracy_score(onlyIndices, prediction)
    print("Accuracy:   %0.3f" % score)
    return prediction

def testEquations(classifier, labeled_data):
    correctly_found = 0
    incorrectly_found = 1
    for (i, iIndex, wordproblem, equationTemplate, solution) in labeled_data:
        foundIndex = classifier.classify(extractFeatures(wordproblem))
        #print foundIndex, i
        if foundIndex == i:
            correctly_found += 1
        else:
            incorrectly_found += 1
    return (correctly_found, incorrectly_found)


