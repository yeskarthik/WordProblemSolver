def generateEquationTemplate(equations):
	numberIndex = 0
	numberSlot = 'n'
	nounSlot = 'x'
	template = []
	numerSlots = {}
	duplicates = {}
	for equation in equations:
		#print equation
		if '0.01' in equation:
			equation = equation.replace("0.01","%")
			#print equation
		sNum = True
		sAlpha = True
		result = ''
		nouns=[]
		curNumber = ''
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
				if curNumber != '':
					if numberSlot+str(numberIndex) not in numerSlots.keys():
						numerSlots[numberSlot+str(numberIndex-1)] = curNumber
					else:
						numerSlots[numberSlot+str(numberIndex-1)] = curNumber
				curNumber = ''
				curNoun += char
				sAlpha = False
			elif char.isnumeric() or char == '.':
				#print 'curnumber:'+ str(curNumber)
				#print 'char'+ str(char)
				curNumber += char
				#print curNumber
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
				if curNumber != '':
					if numberSlot+str(numberIndex) not in numerSlots.keys():
						numerSlots[numberSlot+str(numberIndex-1)] = curNumber
					else:
						numerSlots[numberSlot+str(numberIndex-1)] = curNumber
				curNumber = ''

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
		if curNumber != '':
			if numberSlot+str(numberIndex) not in numerSlots.keys():
				numerSlots[numberSlot+str(numberIndex-1)] = curNumber
			else:
				numerSlots[numberSlot+str(numberIndex-1)] = curNumber
				curNumber = ''
		result = result.replace("%","0.01")
		template.append(result)
	#print numerSlots
	#print template
	for key, value in numerSlots.items():
		if value not in duplicates:
			duplicates[value] = [key]
		else:
			duplicates[value].append(key)
	#print duplicates
	valueToReplace = ''
	toBeReplaced = ''
	for key, value in duplicates.items():
		if len(value) == 2:
			valueToReplace = value[0]
			toBeReplaced = value[1]
			for i in range(0,len(template)):
				if toBeReplaced in template[i]:
					template[i] = template[i].replace(toBeReplaced, valueToReplace)
					break
				else:
					pass
		else:
			pass
	#print 'final: '
	#print  template
	return template
	#print result
	#print nouns



#generateEquationTemplate([u'((6.0*0.01)*six_acid)+((14.0*0.01)*fourteen_acid)=12.0*0.01*50.0',u'six_acid+fourteen_acid=50.0'])

