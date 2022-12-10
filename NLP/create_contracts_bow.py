import pandas as pd
import numpy as np
import string
import nltk
import time
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

wnl = WordNetLemmatizer ()
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))
punct_list = string.punctuation

'''FORMAT DATA FOR DUPLICATE DETECTION'''

#read in contracts data as dataframe
def load_data_file(path):
    target_file = "Contracts_master.csv"
    target_path = path + target_file
    contracts_df = pd.read_csv(target_path, encoding = 'utf-8-sig')#.set_index('VENDOR_KEY')
    return(contracts_df)

'''Take in a list of docs and output a pre-processed list of clean docs'''

#sentence = contracts_df['CONTRACT_TITLE'][100]

#preprocess string into clean string
def remove_punct_string(sentence):
    punct_list = string.punctuation
    clean_sentence = ''.join(c if c not in punct_list else ' ' for c in sentence)
    return(clean_sentence.lower())

#no_punct_sentence = remove_punct_string(sentence)

def preprocess_string(sentence):
    clean_string = ""
    total_words = len(sentence.split())
    word_count = -1
    for word in sentence.split():
        word_count += 1
        if word.isalpha() and word not in stop_words:
            word = wnl.lemmatize(word)
            word = ps.stem(word)
            if word_count < total_words:
                clean_string += word + " "
            else:
                clean_string += word
    return(clean_string)

#clean_string = preprocess_string(no_punct_sentence)

'''from a list of docs, create a bag of words'''

#tokenize each sentence in a list of sentences
def list_tokens(sentence):
    token_list = []
    for word in sentence.split():
        if word.isalpha() and word not in stop_words:
            token_list.append(word)
    return(token_list)

#clean each sentence in list of sentences
def preprocess_list(contracts_list):
    contracts_list_clean = []
    for sentence in contracts_list:
        no_punct_string = remove_punct_string(sentence)
        clean_string = preprocess_string(no_punct_string)
        contracts_list_clean.append(clean_string)
    return(contracts_list_clean)

#contracts_list_clean = preprocess_list(contracts_list)

def create_tokens_list_of_list(contracts_list_clean):
    list_of_tokens_list = []
    for sentence in contracts_list_clean:
        sentence_tokens = list_tokens(sentence)
        list_of_tokens_list.append(sentence_tokens)
    return(list_of_tokens_list)

#list_of_tokens_list = create_tokens_list_of_list(contracts_list_clean)

'''create a bag of words from a list of documents'''
#create bag of words
def create_dictionary_of_tokens(list_of_tokens_list):
    wordfreq = {}
    for list in list_of_tokens_list:
        for token in list:
            if token not in wordfreq.keys():
                wordfreq[token] = 1
            else:
                wordfreq[token] += 1
    return(wordfreq)

#word_freq_dict = create_dictionary_of_tokens(list_of_tokens_list)

#contracts_list = contracts_df['CONTRACT_TITLE'][0:10]
#contracts_list_clean = preprocess_list(contracts_list)

def create_bow_from_doc_list(contracts_list_clean):
    list_of_tokens_list = create_tokens_list_of_list(contracts_list_clean)
    word_freq_dict = create_dictionary_of_tokens(list_of_tokens_list)
    return(word_freq_dict)
    
#word_freq_dict = create_bow_from_doc_list(contracts_list_clean)

'''build the bag-of-words model'''

def build_bow_model(contracts_list_clean, word_freq_dict):
    start_time = time.perf_counter()
    print('\nQuery Running...\n')
    X = []
    for sentence in contracts_list_clean:
        vector = []
        for word in word_freq_dict.keys():
            if word in sentence.split():
                vector.append(1)
            else:
                vector.append(0)
        X.append(vector)
    end_time = time.perf_counter()
    total_time = (end_time - start_time)
    output_str = "Query finished in {} seconds".format(round(total_time, 2))
    print(output_str)
    return(X)
#X = build_bow_model(contracts_list_clean, word_freq_dict)

#print dataframe
def format_bow_df(X, word_freq_dict, contracts_df):
    col_names = word_freq_dict.keys()
    df1 = pd.DataFrame(columns=col_names)
    index = -1
    count = 0
    for i in X:
        index += 1
        count += 1
        df1.loc[len(df1)] = X[index]
        if count == 1000:
            msg= '\n {} rows completed'.format(index+1)
            print(msg)
            count = -1
    df2 = contracts_df['CONTRACT_NO']
    df3 = pd.concat([df2, df1], axis = 1)
    return(df3)


path = "../Outputs/"
contracts_df = load_data_file(path)
contracts_list = contracts_df['CONTRACT_TITLE']
contracts_list_clean = preprocess_list(contracts_list)
word_freq_dict = create_bow_from_doc_list(contracts_list_clean)
X = build_bow_model(contracts_list_clean, word_freq_dict)
X = np.asarray(X)
df = format_bow_df(X, word_freq_dict, contracts_df)
bow_to_csv = df.to_csv(path + "contracts_bow.csv", index = False)