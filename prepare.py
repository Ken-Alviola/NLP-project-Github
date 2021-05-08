import unicodedata
import re
import json
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('wordnet')



def basic_clean(text):
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ascii','ignore').decode('utf-8','ignore')
    text = re.sub(r"[^a-z0-9'\s]",'',text)
    return text


def tokenize(text):
    tokenizer = nltk.tokenize.ToktokTokenizer()
    text = tokenizer.tokenize(text, return_str=True)
    return text

def stem(text):
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in text.split()]
    text_stemmed = ' '.join(stems)
    return text_stemmed

def lemmatize(text):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in text.split()]
    text_lemmatized = ' '.join(lemmas)
    return text_lemmatized

def remove_stopwords(text, extra_words=[], exclude_words=[]):
    #nltk.download('stopwords')
    stopword_list = stopwords.words('english')
    if len(extra_words) > 0 :
        for word in extra_words:
            stopword_list.append(word)
    if len(exclude_words) > 0:
        for word in exclude_words:
            stopword_list.remove(word)
    words = text.split()
    filtered_words = [word for word in words if word not in stopword_list]
    text_without_stopwords = ' '.join(filtered_words)
    return text_without_stopwords    

def split(df, stratify_by=None):
    """
    3 way split for train, validate, and test datasets
    To stratify, send in a column name
    """
    train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[stratify_by])
    
    train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train[stratify_by])
    
    return train, validate, test