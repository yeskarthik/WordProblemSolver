def generateEquationTemplate(equations):
	numberIndex = 0
	numberSlot = 'n'
	nounSlot = 'x'
	template = []
	for equation in equations:
		#print equation
		if '0.01' in equation:
			equation = equation.replace("0.01","%")
			#print equation
		sNum = True
		sAlpha = True
		result = ''
		nouns=[]
		curNoun = ''
		prev_char = ''
		for char in equation:
			#print char
			if(char == '%'):
				pass
			if char.isalpha() or char == '_' or (char.isnumeric() and (prev_char.isalpha() or prev_char == '_')):
				if(sAlpha == True):
					sNum = True
				else:
					pass
				curNoun += char
				sAlpha = False
			elif char.isnumeric() or char == '.':
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
			else:	
				if curNoun != '':
					if curNoun not in nouns:
						nouns.append(curNoun)
					result += nounSlot + str(nouns.index(curNoun))
					curNoun = ''
				sNum = True
				result += char
				sAlpha = True
			prev_char = char
		if equation[-1].isalpha():
			if curNoun not in nouns:
				nouns.append(curNoun)
			result += nounSlot + str(nouns.index(curNoun))
		result = result.replace("%","0.01")
		template.append(result)
	print template
	return template
	#print result
	#print nouns



#generateEquationTemplate([u'(7*0.01*fundone)+(6*0.01*fundtwo)=405.0'])

