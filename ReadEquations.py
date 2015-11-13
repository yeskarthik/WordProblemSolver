def generateEquationTemplate(equations):
	numberIndex = 0
	numberSlot = 'n'
	nounSlot = 'x'
	template = []
	for equation in equations:
		#print equation
		sNum = True
		sAlpha = True
		result = ''
		nouns=[]
		curNoun = ''
		for char in equation:
			#print char
			if char.isnumeric() or char == '.':
				if sNum == True:				
					if curNoun != '':
						if curNoun not in nouns:
							nouns.append(curNoun)
						result += nounSlot + str(nouns.index(curNoun))
						curNoun = ''
					sAlpha = True
					result += numberSlot + str(numberIndex)
					numberIndex += 1
				else:
					pass
				sNum = False
			elif char.isalpha() or char == '_':
				if(sAlpha == True):
					sNum = True
				else:
					pass
				curNoun += char
				sAlpha = False
			else:	
				if curNoun != '':
					if curNoun not in nouns:
						nouns.append(curNoun)
					result += nounSlot + str(nouns.index(curNoun))
					curNoun = ''
				sNum = True
				result += char
				sAlpha = True
		if equation[-1].isalpha():
			if curNoun not in nouns:
				nouns.append(curNoun)
			result += nounSlot + str(nouns.index(curNoun))
		template.append(result)
	return template
		#print result
		#print nouns



#generateEquationTemplate([u'3.0*novelists=5.0*poets', u'novelists+poets=24.0'])

