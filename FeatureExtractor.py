import nltk
import sklearn
import numpy

from nltk.tag.perceptron import PerceptronTagger
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import WordNetLemmatizer

class LemmaTokenizer(object):
    def __init__(self):
        self.wnl = WordNetLemmatizer()
    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in nltk.word_tokenize(doc)]


tagger = PerceptronTagger()

def addBagOfWordsFeature(wordproblems):
    vectorizer = CountVectorizer(analyzer = 'word', tokenizer=LemmaTokenizer(), preprocessor = None, 
        stop_words = None, max_features = 5000)
    train_data_features = vectorizer.fit_transform(wordproblems)    
    train_data_features = train_data_features.toarray()
    vocab = vectorizer.get_feature_names()
    vocab_wo_nums = []
    for s in vocab:
        if not any(char.isdigit() for char in s):
            vocab_wo_nums.append(s)
        else:
            print s

    vectorizer = CountVectorizer(analyzer = 'word', tokenizer=LemmaTokenizer(), preprocessor = None, 
        stop_words = None, max_features = 5000, vocabulary = vocab_wo_nums)

    train_data_features = vectorizer.fit_transform(wordproblems)    
    train_data_features = train_data_features.toarray()
    vocab = vectorizer.get_feature_names()

    with open('data/vocab.txt', 'w') as f:
        f.write(str(vocab_wo_nums))

    numofnums = []
    numofques = []
    numofpercent = []
    for i in range(0, len(train_data_features)):
        nums = numberOfNumbers(None, wordproblems[i])
        numofnums.append(nums)
        ques = numberOfQuestions(wordproblems[i])
        numofques.append(ques)
        perc = numberOfPercent(wordproblems[i])
        numofpercent.append(perc)
    numofnums = numpy.array(numofnums)
    numofques = numpy.array(numofques)
    numofpercent = numpy.array(numofpercent)

    train_data_features = numpy.hstack((train_data_features, numpy.atleast_2d(numofnums).T))
    train_data_features = numpy.hstack((train_data_features, numpy.atleast_2d(numofques).T))
    train_data_features = numpy.hstack((train_data_features, numpy.atleast_2d(numofpercent).T))

    #print train_data_features
    return (vectorizer, train_data_features)


def addFeature(features, feature):
        try:
            features[feature] = features[feature] + 1
        except KeyError:
            features[feature] = 1

def numberOfNumbers(features, wordProblem):
    count = 0
    
    tagset = None
    tokens = nltk.word_tokenize(wordProblem)
    tags = nltk.tag._pos_tag(tokens, tagset, tagger)
    
    for word, pos in tags:
        if pos == 'CD':
            if features != None:
                addFeature(features, 'NUM_OF_NUMS')
            count += 1
    return count

def numberOfQuestions(wordProblem):
    count =0
    tokens = nltk.word_tokenize(wordProblem)
    for word in tokens:
        word = word.lower()
        if('?' in word or 'find' in word):
            count += 1
    return count

def numberOfPercent(wordProblem):
    count =0
    tokens = nltk.word_tokenize(wordProblem)
    for word in tokens:
        word = word.lower()
        if '%' in word or 'percent' in word or 'percentage' in word:
            count += 1
    return count    

def extractScikitFeatures(wordProblem):
    pass

def extractFeatures(wordProblem):    

    features = {}

    for word in nltk.word_tokenize(wordProblem):
        word = word.lower()

        if '$' in word: #Not so useful
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
        if 'interest' in word: #Not so useful
            addFeature(features, 'INTEREST')
        if 'find' in word or '?' in word:
            addFeature(features, 'QUESTION')
        if 'sum' in word:
            addFeature(features, 'SUM')
        if 'difference' in word: #Not so useful
            addFeature(features, 'DIFFERENCE')
        if 'between' in word: #Not so useful
            addFeature(features, 'BETWEEN')
        if 'many' in word:
            addFeature(features, 'MANY')
        if 'ratio' in word:
            addFeature(features, 'RATIO')
        #if 'numbers' in word or 'number' in word:
        #    addFeature(features, 'NUMSTR')


    numberOfNumbers(features, wordProblem)
    #print features

    return features

#print extractFeatures('A writing workshop enrolls novelists and poets in a ratio of 5 to 3. There are 24 people at the workshop. How many novelists are there? How many poets are there?')
#print extractFeatures('Flying with the wind , a bird was able to make 150 kilometers per hour. If the wind was 0.5 times as strong and the bird flies against it , it could make only 30 kilometers per hour. Find the velocity of the wind in kilometers per hour. Find the velocity of the bird. ')