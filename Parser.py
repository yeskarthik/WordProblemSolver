import json
from ReadEquations import generateEquationTemplate
from Classifier import trainClassifier, trainClassifierScikit
from TestEquations import testEquations, testScikitEquations
from AlignmentClassifier import trainAlignmentClassifier, trainAlignmentClassifierScikit
from TestAlignment import testAlignments

data = None
labeled_data = []
allTemplates = []
def parseDataset(dataSource):
    templates = []
    
    with open(dataSource, 'r') as f:
        data = json.loads(f.read())

        for wordproblem in data:
            iIndex = wordproblem['iIndex']
            sQuestion = wordproblem['sQuestion']
            lEquations = wordproblem['lEquations']
            lSolutions = wordproblem['lSolutions']

            template = generateEquationTemplate(lEquations)
            
            if template not in allTemplates:
                allTemplates.append(template)
                templates.append((allTemplates.index(template), iIndex, sQuestion, template, lSolutions))
                labeled_data.append((allTemplates.index(template), iIndex, sQuestion, template, lSolutions))
            else:                
                labeled_data.append((allTemplates.index(template), iIndex, sQuestion, template, lSolutions))

    return templates

def segregateByTemplates(labeled_data):
    result = {}
    for i, iIndex, sQuestion, template, lSolutions in labeled_data:
        try:
            result[str(template)].append((i, iIndex, sQuestion, template, lSolutions))
        except:
            result[str(template)] = [(i, iIndex, sQuestion, template, lSolutions)]
    return result



if __name__ == "__main__":
    labeled_word_problems = parseDataset('data/questions-original.json')
    
    with open('data/templates.txt', 'w') as f:
        for i, iIndex, sQuestion, template, lSolutions in labeled_data:
            f.write(str(i) + ' , ' + str(iIndex) + ' , ' + str(template) + ' , ' + sQuestion + ',' + '\n')
    
    #Divide into two folds
    length_by_two = len(labeled_data)/2
    train_data = labeled_data[:length_by_two]
    test_data = labeled_data[length_by_two:]

    #train_data = train_data[:50]
    #test_data = train_data
    
    #train_data = labeled_data[length_by_two:]
    #test_data = labeled_data[:length_by_two]
    
    #classifier = trainAlignmentClassifierScikit(train_data, 'NaiveBayes')
    #print classifier

    
    #algorithmsNLTK = ['NaiveBayes', 'DecisionTree', 'MaxEnt', 'MaxEntMegam']
    #algorithmsSciKit = ['NaiveBayes', 'DecisionTree', 'SVM', 'MaxEnt']
    '''
    algorithmsNLTK = []
    algorithmsSciKit = ['NaiveBayes']

    print 'Start..'
    for algorithm in algorithmsSciKit:
        print 'Using', algorithm, 'classifier - Scikit Learn'  
        (vectorizer, classifier) = trainClassifierScikit(train_data, algorithm)
        predictedEquations = testScikitEquations(classifier, vectorizer, test_data)


    for algorithm in algorithmsNLTK:
        classifier = trainClassifier(train_data, algorithm)
        stats = testEquations(classifier, test_data)
        print 'Using', algorithm, 'classifier - NLTK'        
        print 'Accuracy:', stats[0]/(stats[0]+stats[1]+0.0)
        #print 'Incorrectly predicted:', stats[1]/(stats[0]+stats[1]+0.0)

    print 'End.'

    

    classifier = trainAlignmentClassifierScikit(train_data, 'NaiveBayes')
    predictedAlignment = testAlignments(test_data,classifier)
    print predictedAlignment
    #print classifier
    '''

    train_by_templates = segregateByTemplates(train_data)

    l = [(len(train_by_templates[key]), key) for key in train_by_templates.keys()]
    training_templates = list(reversed(sorted(l, key = lambda t: t[0])))

    classifiers = {}
    
    for tid, tem in training_templates:

        classifier = trainAlignmentClassifierScikit(train_by_templates[tem], 'NaiveBayes')
        classifiers[tem] = classifier
        print classifier

    predictedAlignment = testAlignments(test_data, classifiers)
    print predictedAlignment

    print training_templates





    