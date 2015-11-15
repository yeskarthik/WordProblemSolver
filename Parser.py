import json
from ReadEquations import generateEquationTemplate
from Classifier import trainClassifier, trainClassifierScikit
from TestEquations import testEquations

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
    #print labeled_word_problems
    with open('data/templates.txt', 'w') as f:
        for i, iIndex, sQuestion, template in labeled_data:
            f.write(str(i) + ' , ' + str(iIndex) + ' , ' + str(template) + '\n')
    #print labeled_data
    #Divide into two folds
    length_by_two = len(labeled_data)/2
    train_data = labeled_data[:length_by_two]
    test_data = labeled_data[length_by_two:]
    
    algorithms = ['NaiveBayes', 'DecisionTree', 'MaxEntMegam']
    #algorithms = ['NaiveBayes']

    print 'Start..'
    #classifier = trainClassifierScikit(train_data, 'NaiveBayes')
    for algorithm in algorithms:
        classifier = trainClassifier(train_data, algorithm)
        stats = testEquations(classifier, test_data)
        print algorithm
        print stats
        print 'Correctly predicted:', stats[0]/(stats[0]+stats[1]+0.0)*100.0,'%'
        print 'Incorrectly predicted:', stats[1]/(stats[0]+stats[1]+0.0)*100.0,'%'
    #print allTemplates[chosen_template_index]

    #for i, iIndex, sQuestion, template in labeled_data:
    #    print i, iIndex, template
    print 'End.'

#print data

    