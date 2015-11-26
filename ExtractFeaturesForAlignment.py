import nltk
from nltk.tag.perceptron import PerceptronTagger
tagger = PerceptronTagger()
def extractNumberVectorFromQuestion(wordproblem):
	numberVector = []	
	tokens = nltk.word_tokenize(wordproblem)
	tagset = None
	tags = nltk.tag._pos_tag(tokens, tagset, tagger)
	for word, pos in tags:
		if pos == 'CD':
			number = convertNumber(unicode(word,"utf-8"))
			#print number
			numberVector.append(number)
		else:
			pass
	print numberVector



def convertNumber(word):
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
		current = result = 0
		for word in textnum.split():
			if word not in numwords:
				raise Exception("Illegal word: " + word)
			scale, increment = numwords[word]
			current = current * scale + increment
			if scale > 100:
				result += current
				current = 0
	return result + current



extractNumberVectorFromQuestion("A woman invested a total of 9,000 dollars in 2 accounts , one earning 6.5 % annual interest and the other earning 8 % annual interest.")
