import nltk
from FeatureExtractor import extractFeatures


def trainClassifierScikit(labeled_word_problems, algorithm):
    featuresets = [(extractFeatures(wordproblem), i) for (i, iIndex, wordproblem, equationTemplate) in labeled_word_problems]

    for featureset in featuresets:
        feat = []
        print featureset
        for key in featureset[0].keys():
            feat.append(featureset[key])
            print feat

def trainClassifier(labeled_word_problems, algorithm):
    
    featuresets = [(extractFeatures(wordproblem), i) for (i, iIndex, wordproblem, equationTemplate) in labeled_word_problems]

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

    #chosen_template = classifier.classify(extractFeature('Marc sold 563 tickets for the school play. Student tickets cost 4 dollars and adult tickets cost 6 dollars. Marc \'s sales totaled 2840 dollars. How many adult tickets and student tickets did Marc sell? '))

    #return chosen_template