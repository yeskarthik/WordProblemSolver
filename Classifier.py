import nltk
from FeatureExtractor import extractFeature

def classify(labeled_word_problems):
    
    featuresets = [(extractFeature(wordproblem), i) for (i, iIndex, wordproblem, equationTemplate) in labeled_word_problems]

    train_set = featuresets

    classifier = nltk.DecisionTreeClassifier.train(train_set)

    #return classifier

    chosen_template = classifier.classify(extractFeature('Marc sold 563 tickets for the school play. Student tickets cost 4 dollars and adult tickets cost 6 dollars. Marc \'s sales totaled 2840 dollars. How many adult tickets and student tickets did Marc sell? '))

    return chosen_template