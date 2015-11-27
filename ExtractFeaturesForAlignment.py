import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tag.perceptron import PerceptronTagger
from TemplateParser import solveEquations, getNumberslots
from sympy import Symbol

tagger = PerceptronTagger()

keywords = {"zero":0, "one":1, "two":2,"twice":2, "thrice":3, "double":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8,
		"nine":9, "ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15,
		"sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19, "triple":3}

def extractNumberVectorFromQuestion(wordproblem):
	percents = 0

	sentences = wordproblem.replace('?','. ').split('. ')
	numberVector = []
	for i in range(0, len(sentences)):
		sentence = sentences[i]
		sentence = sentence.replace('-', ' ')
		#tokens = tokenizer.tokenize(sentence)
		tokens = nltk.word_tokenize(sentence)
		tagset = None
		tags = nltk.tag._pos_tag(tokens, tagset, tagger)
		for wordIndex in range(0,len(tags)):
			word, pos = tags[wordIndex]
			#print wordIndex, word, pos
			try:
				if word.lower() == 'one':
					nextword, nexttag = tags[wordIndex+1]
					#prevword, pretag = tags[wordIndex+1]
					if nexttag != 'JJR':
						continue
			except:
				pass
			if word.lower() in keywords.keys():
				numberVector.append(keywords[word.lower()])
			#print word, pos
			elif pos == 'CD':
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
			#elif word == '%':
			#	percents += 1
			#	if percents < 3:
			#		numberVector.append(0.01)
	if '%' in wordproblem.lower() or 'cents' in wordproblem.lower() or 'percent' in wordproblem.lower() or 'percentage' in wordproblem.lower():
		numberVector.append(0.01)
	elif 'dimes' in wordproblem.lower():
		numberVector.append(0.1)		
	elif 'nickels' in wordproblem.lower():
		numberVector.append(0.05)
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
		#print result
		return result



def text2int(textnum, numwords={}):
	current = result = 0
	textnum = str(textnum).lower()
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

#wordproblem = 'Nine books are to be bought by a student'
#equation = [u'(n0*x0)-(n1*x1)=n2', u'x0+x1=n3'] 
#solution = [19.0]
#print findAlignment(wordproblem, equation, solution)
#extractNumberVectorFromQuestion("A student is pricing 2 different picture packages. John 's Photo World charges 2.75 dollars per sheet and a one time sitting fee of 125 dollars. Sam 's Picture Emporium charges 1.50 dollars per sheet and a one time sitting fee of 140 dollars. For how many sheets of pictures do the 2 companies charge the same amount?")
