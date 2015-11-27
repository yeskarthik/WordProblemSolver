from TemplateParser import  getNumberslots
from ExtractFeaturesForAlignment import extractNumberVectorFromQuestion, findAlignment

def extractAlignmentFeatures(wordproblems):
	question = wordproblem['sQuestion']
	featureVector = []
	for wordproblem in wordproblems:
		numberVector = extractNumberVectorFromQuestion(wordproblem['sQuestion'])
		noOfNumberSlots = len(getNumberslots(wordproblem['lEquations']))
		solutionFeature = wordproblem['lSolutions']
		correctAlignment = findAlignment(question)