import nltk

def addFeature(features, feature):
        try:
            features[feature] = features[feature] + 1
        except KeyError:
            features[feature] = 1

def numberOfNumbers(features, wordProblem):
    count = 0
    tagged = nltk.pos_tag(nltk.word_tokenize(wordProblem))
    for word, pos in tagged:
        if pos == 'CD':
            addFeature(features, 'NUM_OF_NUMS')
    return count

def extractFeature(wordProblem):    

    features = {}

    for word in nltk.word_tokenize(wordProblem):
        word = word.lower()

        if '$' in word:
            addFeature(features, 'DOLLAR')
        if '%' in word or 'percent' in word or 'percentage' in word:
            addFeature(features, 'PERCENTAGE')
        if 'total' in word or 'together' in word or 'divided' in word or 'parts' in word:
            addFeature(features, 'TOTAL')
        if 'than' in word or 'increased' in word or 'decreased' in word:
            addFeature(features, 'THAN')
        if 'twice' in word or 'thrice' in word or 'times' in word:
            addFeature(features, 'TIMES')
        if 'miles' in word:
            addFeature(features, 'MILES')
        if 'interest' in word:
            addFeature(features, 'INTEREST')
        if 'find' in word or '?' in word:
            addFeature(features, 'QUESTION')
        if 'sum' in word:
            addFeature(features, 'SUM')
        if 'difference' in word:
            addFeature(features, 'DIFFERENCE')
        if 'between' in word:
            addFeature(features, 'BETWEEN')

    numberOfNumbers(features, wordProblem)
    #print features

    return features

print extractFeature('A writing workshop enrolls novelists and poets in a ratio of 5 to 3. There are 24 people at the workshop. How many novelists are there? How many poets are there?')
print extractFeature('Flying with the wind , a bird was able to make 150 kilometers per hour. If the wind was 0.5 times as strong and the bird flies against it , it could make only 30 kilometers per hour. Find the velocity of the wind in kilometers per hour. Find the velocity of the bird. ')