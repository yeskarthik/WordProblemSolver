from FeatureExtractor import extractFeatures

def testEquations(classifier, labeled_data):
    correctly_found = 0
    incorrectly_found = 1
    for (i, iIndex, wordproblem, equationTemplate) in labeled_data:
        foundIndex = classifier.classify(extractFeatures(wordproblem))
        #print foundIndex, i
        if foundIndex == i:
            correctly_found += 1
        else:
            incorrectly_found += 1
    return (correctly_found, incorrectly_found)
