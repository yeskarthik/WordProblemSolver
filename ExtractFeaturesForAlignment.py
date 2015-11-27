import nltk
from nltk.tag.perceptron import PerceptronTagger
from TemplateParser import solveEquations, getNumberslots
from sympy import Symbol

tagger = PerceptronTagger()
def extractNumberVectorFromQuestion(wordproblem):
	percents = 0

	sentences = wordproblem.replace('?','. ').split('. ')
	numberVector = []
	for i in range(0, len(sentences)):
		sentence = sentences[i]
		
		tokens = nltk.word_tokenize(sentence)
		tagset = None
		tags = nltk.tag._pos_tag(tokens, tagset, tagger)
		for word, pos in tags:
			if pos == 'CD':
				#print word
				number = convertToNumber(unicode(str(word),"utf-8"))
				#print number
				try:
					if i > 0:
						numberVector.index(number)
					else:
						numberVector.append(number)
				except ValueError:					
					numberVector.append(number)
			elif word == '%':
				percents += 1
				if percents < 3:
					numberVector.append(0.01)
			else:
				pass
	print 'Extract feature', numberVector
	return numberVector



def convertToNumber(word):
	number = 0.0
	strnum = ''
	flag = False
	#print word
	for char in word:
		if(char.isnumeric() or char == '.'):
			strnum += char
		elif (char == ','):
			pass
		else:
			flag = True
			break
	if(flag == False):
		#print strnum
		return float(strnum)
	else:
		result = text2int(word)
		return result



def text2int(textnum, numwords={}):
	current = result = 0
	if not numwords:
		units = [
		"zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
		"nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
		"sixteen", "seventeen", "eighteen", "nineteen",
		]

		tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
		scales = ["hundred", "thousand", "million", "billion", "trillion"]
		numwords["and"] = (1, 0)
		for idx, word in enumerate(units):    numwords[word] = (1, idx)
		for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
		for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)
		
		for word in textnum.split():
			if word not in numwords:
				raise Exception("Illegal word: " + word)
			scale, increment = numwords[word]
			current = current * scale + increment
			if scale > 100:
				result += current
				current = 0
	return result + current


def createAllAlignments(numberVector):
	alignments = all_perms(numberVector)
	return alignments



def all_perms(elements):
	if len(elements) <=1:
		yield elements
	else:
		for perm in all_perms(elements[1:]):
			for i in range(len(elements)):
				# nb elements[0:1] works in both string and list contexts
				yield perm[:i] + elements[0:1] + perm[i:]


def findAlignment(wordproblem, equation, solution):
	numberVector = extractNumberVectorFromQuestion(wordproblem)
	#numberVector = numberVector[:5]
	alignments = createAllAlignments(numberVector)
	correctAlignment =[]
	x0 = Symbol('x0')
	test = []
	#x1 = Symbol('x1')
	try:
		i = 0
		for alignment in alignments:
			result = solveEquations(equation, getNumberslots(equation), alignment)
			test = alignment
			if len(result) != 0:
				if len(equation) == 1:
					if solution[0] == result[x0]:
						correctAlignment = alignment
				elif len(equation) == 2:
					if solution[0] == result[x0]:# and solution[1] == result[x1]:
						correctAlignment = alignment
	except:
		print 'error'
		print wordproblem
		print equation
		print test


	return (correctAlignment, numberVector)

#wordproblem = 'In a test of 30 questions , 20 points are given for each correct answer and 5 points are deducted for each one answered incorrectly. If Maria answered all of the questions and got a score of 325 , how many did she get correct?'
#equation = [u'(n0*x0)-(n1*x1)=n2', u'x0+x1=n3'] 
#solution = [19.0]
#print findAlignment(wordproblem, equation, solution)
#extractNumberVectorFromQuestion("A woman invested a total of 9,000 dollars in 2 accounts , one earning 6.5 % annual interest and the other earning 8 % annual interest.")
