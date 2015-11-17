import json
from ReadEquations import generateEquationTemplate
from Classifier import trainClassifier, trainClassifierScikit
from TestEquations import testEquations, testScikitEquations

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
                templates.append((allTemplates.index(template), iIndex, sQuestion, template))
                labeled_data.append((allTemplates.index(template), iIndex, sQuestion, template))
            else:                
                labeled_data.append((allTemplates.index(template), iIndex, sQuestion, template))

    return templates


if __name__ == "__main__":
    labeled_word_problems = parseDataset('data/questions-original.json')
    
    with open('data/templates.txt', 'w') as f:
        for i, iIndex, sQuestion, template in labeled_data:
            f.write(str(i) + ' , ' + str(iIndex) + ' , ' + str(template) + ' , ' + sQuestion + '\n')
    
    #Divide into two folds
    length_by_two = len(labeled_data)/2
    train_data = labeled_data[:length_by_two]
    test_data = labeled_data[length_by_two:]

    #train_data = labeled_data[length_by_two:]
    #test_data = labeled_data[:length_by_two]
    
    algorithmsNLTK = ['NaiveBayes', 'DecisionTree', 'MaxEnt', 'MaxEntMegam']
    algorithmsSciKit = ['NaiveBayes', 'DecisionTree', 'SVM', 'MaxEnt']

    print 'Start..'
    for algorithm in algorithmsSciKit:
        print 'Using', algorithm, 'classifier - Scikit Learn'  
        (vectorizer, classifier) = trainClassifierScikit(train_data, algorithm)
        stats = testScikitEquations(classifier, vectorizer, test_data)


    for algorithm in algorithmsNLTK:
        classifier = trainClassifier(train_data, algorithm)
        stats = testEquations(classifier, test_data)
        print 'Using', algorithm, 'classifier - NLTK'        
        print 'Accuracy:', stats[0]/(stats[0]+stats[1]+0.0)
        #print 'Incorrectly predicted:', stats[1]/(stats[0]+stats[1]+0.0)

    print 'End.'



    