import numpy as np
import nltk

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D
from keras.datasets import imdb

nltk.download('punkt')

def tokenizeCode(codeSnippet):
    tokenDict = {
        'printf': 1,
        'scanf': 2,
        '%_d': 3,
        '%_s': 4,
        '``': 5, # NLTK beginning qutation marks 
        "''": 6, # NLTK ending qutation marks
        ',': 7,
        '(': 8,
        ')': 9,
        ';': 10  }

    tokenizer = nltk.tokenize.MWETokenizer()
    tokenizer.add_mwe(('%', 'd'))
    tokenizer.add_mwe(('%', 'n'))

    tokens = tokenizer.tokenize(nltk.word_tokenize(codeSnippet))

    indexedTokens = []
    for token in tokens:
        indexedTokens.append(tokenDict.get(token, 0))
    
    return indexedTokens


x_train = []
y_train = []

x_test = []
x_test_real = []
y_test = []

f = open("./train.txt", "r")
contents = f.readlines()
for i, line in enumerate(contents):
    x_data, y_data = line.strip().split('\t')
    if i % 5 == 0:
        x_test_real.append(x_data)
        x_test.append(tokenizeCode(x_data))
        y_test.append(int(y_data))
    else:
        x_train.append(tokenizeCode(x_data))
        y_train.append(int(y_data))

# set parameters:
max_features = 15
maxlen = 20
batch_size = 32
embedding_dims = 50
filters = 250
kernel_size = 3
hidden_dims = 250
epochs = 3

print('Pad sequences (samples x time)')
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)

print('Build model...')
model = Sequential()

# we start off with an efficient embedding layer which maps
# our vocab indices into embedding_dims dimensions
model.add(Embedding(max_features,
                    embedding_dims,
                    input_length=maxlen))
model.add(Dropout(0.2))

# we add a Convolution1D, which will learn filters
# word group filters of size filter_length:
model.add(Conv1D(filters,
                 kernel_size,
                 padding='valid',
                 activation='relu',
                 strides=1))
# we use max pooling:
model.add(GlobalMaxPooling1D())

# We add a vanilla hidden layer:
model.add(Dense(hidden_dims))
model.add(Dropout(0.2))
model.add(Activation('relu'))

# We project onto a single unit output layer, and squash it with a sigmoid:
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_data=(x_test, y_test))


realTest = [
    'printf("Hey %s, how are you?", name);',
    'printf("Doing fine...");',
    'printf(status);',
    'printf("What about you?");',
    'printf("");',
]

tokenizedTest = []

for test in realTest:
    tokenizedTest.append(tokenizeCode(test))

tokenizedTest = sequence.pad_sequences(tokenizedTest, maxlen=maxlen)
results = model.predict(tokenizedTest)

for i in range(len(tokenizedTest)):
    print(realTest[i])
    print(results[i])
