import json
from ReadEquations import generateEquationTemplate
from Classifier import classify

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
    print labeled_word_problems
    for i, iIndex, sQuestion, template in labeled_word_problems:
        print iIndex, template
    #print labeled_data
    chosen_template_index = classify(labeled_data)
    print allTemplates[chosen_template_index]

    #for i, iIndex, sQuestion, template in labeled_data:
    #    print i, iIndex, template


#print data

    