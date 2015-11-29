import nltk
import numpy

from AlignmentFeatures import extractAlignmentFeatures

from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression


def trainAlignmentClassifierScikit(labeled_word_problems, algorithm):
    
    featuresets = []
    correctlyAlignedIndicesList = []
    for (i, iIndex, wordproblem, equationTemplate, solution) in labeled_word_problems:
        print iIndex
        alignmentFeatures, correctlyAlignedIndices = extractAlignmentFeatures(wordproblem, equationTemplate, solution, i, 'train')

        if len(correctlyAlignedIndices) != 0 and len(alignmentFeatures) != 0:
            featuresets.append(alignmentFeatures)
            alignedString = '' 
            for i in correctlyAlignedIndices:
                alignedString += str(i)

            correctlyAlignedIndicesList.append(alignedString)

    #sfeaturesets = numpy.array(featuresets)
    print type(featuresets)
    #correctlyAlignedIndicesList = numpy.array(correctlyAlignedIndicesList)


    print featuresets
    print correctlyAlignedIndicesList

    classifier = None

    if len(featuresets) != 0:
        if algorithm == 'SVM':
            classifier = SVC()
        elif algorithm == 'NaiveBayes':
            classifier = GaussianNB()
        elif algorithm == 'DecisionTree':
            classifier = DecisionTreeClassifier()
        elif algorithm == 'MaxEnt':
            classifier = LogisticRegression()

        classifier.fit(featuresets, correctlyAlignedIndicesList)

    return classifier



def trainAlignmentClassifier(labeled_word_problems, algorithm):
    
    featuresets = []
    for (i, iIndex, wordproblem, equationTemplate, solution) in labeled_word_problems:
        alignmentFeatures, correctlyAlignedIndices = extractAlignmentFeatures(wordproblem, equationTemplate, solution, i)
        if len(correctlyAlignedIndices) != 0:
            featuresets.append((alignmentFeatures, correctlyAlignedIndices))
        
        #featuresets = [(extractAlignmentFeatures(wordproblem, equationTemplate, solution), i) 
        #for (i, iIndex, wordproblem, equationTemplate, solution) in labeled_word_problems]

    print featuresets
    train_set = featuresets

    if algorithm == 'DecisionTree':
        classifier = nltk.DecisionTreeClassifier.train(train_set)
    elif algorithm == 'NaiveBayes':
        classifier = nltk.NaiveBayesClassifier.train(train_set)
    elif algorithm == 'MaxEntMegam':
        classifier = nltk.classify.MaxentClassifier.train(train_set, 'MEGAM', trace=0, max_iter=1)
    elif algorithm == 'MaxEnt':
        classifier = nltk.MaxentClassifier.train(train_set)

    return classifier


