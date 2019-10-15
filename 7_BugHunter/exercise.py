''' 
Please read the README.md for Exercise instructions!
'''


# This is the "source code" you want to test.
sourceCode = [
    'printf("Hey %s, how are you?", name);',
    'printf("Doing fine...");',
    'printf(status);',
    'printf("What about you?");',
    'printf("");',
]


# Hmmm, this might be interesting.

import nltk

nltk.download('punkt')

def tokenizeCode(someCode):
    tokenDict = {
        'aaa': 1,
        'bbb': 2  }

    tokenizer = nltk.tokenize.MWETokenizer()
    tokens = tokenizer.tokenize(nltk.word_tokenize(someCode))

    indexedTokens = []
    for token in tokens:
        indexedTokens.append(tokenDict.get(token, 0))
    
    return indexedTokens

