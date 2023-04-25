#Text Data Preprocessing Lib
import nltk

# function for appending stem words
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

import json
import pickle 
import numpy as np

words = []
classes = []
word_tag_list=[]
ignore_words = ['?','!','.',',',"'s","'m"]
train_data_file = open('intents.json').read()
intents = json.loads(train_data_file)

def get_stem_words(words, ignore_words):
    stem_words=[]
    for word in words:
        if word not in ignore_words:
            w = stemmer.stem(word.lower())
            stem_words.append(w)
        return stem_words
    
for intent in intents['intents']:
    
    for pattern in intent['patterns']:
        pattern_word = nltk.word_tokenize(pattern)
        words.extend(pattern_word)
        word_tag_list.append((pattern_word, intent['tag']))
    if intent['tag'] not in classes:
        classes.append(intent['tag'])
        stem_words = get_stem_words(words, ignore_words)

print(stem_words)
print(word_tag_list[0])
print(classes)

def create_bot_corpus(stem_words, classes):
    stem_words = sorted(list(set(stem_words)))
    classes = sorted(list(set(classes)))

    pickle.dump(stem_words, open('words.pkl','wb'))
    pickle.dump(classes, open('words.pkl','wb'))

    return stem_words, classes

stem_words, classes = create_bot_corpus(stem_words, classes)

print(stem_words)
print(classes)
