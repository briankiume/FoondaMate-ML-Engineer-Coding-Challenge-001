import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk import pos_tag

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def label_filter(sentence):
    # Tokenization
    tokenized = word_tokenize(sentence)

    # Stemming
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(x) for x in tokenized]
    if ('share' in stemmed) & ('email' in tokenized):
        parsed = pos_tag(tokenized)
        
        group = 0
        for tagged in parsed:
            if (tagged[1] == 'VBD') | (tagged[1] == 'VBN'):
                group = 1
        if group == 0:
            label = 'Student wants to know if can share'
        else:
            label = 'Student has shared'
        return label


text = input('Pass a sentence: ')
print(label_filter(text))
