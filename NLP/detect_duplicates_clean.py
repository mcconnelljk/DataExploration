import math
import pandas as pd
import nltk
import time
from nltk.tokenize import word_tokenize, sent_tokenize

#read in and format vendors data as dataframe
path = "../../Tables/"
target_file = "Vendor.csv"
target_path = path + target_file
vendors_df = pd.read_csv(target_path, encoding = 'utf-8-sig')#.set_index('VENDOR_KEY')
vendors_df['VENDOR_NAME'] = vendors_df['VENDOR_NAME'].str.upper()
vendors_df = vendors_df.drop(['REGISTRATION_TYPE', 'VENDOR_ID', 'VENDOR_ADDRESS'], axis = 1)

#read in and format vendor_formatted_address data as dataframe
target_file = "VendorHasAddress.csv"
target_path = path+target_file
vendor_addr_df = pd.read_csv(target_path, encoding = 'utf-8-sig')#.set_index('VENDOR_KEY')
#vendor_addr_df = vendor_addr_df.drop(['VENDOR_CITY', 'VENDOR_STATE', 'VENDOR_ZIP', 'VENDOR_UNIT'], axis = 1)

#join tables and format datasets
vendors_df = vendors_df.merge(vendor_addr_df, how = 'outer', left_on = 'VENDOR_KEY', right_on = 'VENDOR_KEY')
vendors_df['VENDOR_NAME_AND_STREET'] = vendors_df['VENDOR_NAME'].map(str) + ' ' + vendors_df['VENDOR_STREET'].map(str)
vendors_df['PARENT_KEY'] = ''

#
vendors_df2 = vendors_df[0:99]

my_df = vendors_df
data = my_df['VENDOR_NAME']
#docs = list(my_df['VENDOR_NAME'])

index_i = 0
array = data

def detect_near_duplicates(index_i, array):
    i = array[index_i]
    row_list = []
    col_list = []
    index_j = -1
    for j in array:
        index_j += 1
        tokens_i = nltk.word_tokenize(i)
        tokens_j = nltk.word_tokenize(j)
        distance_J_letters = nltk.jaccard_distance(set(i), set(j))
        distance_J_words = nltk.jaccard_distance(set(tokens_i), set(tokens_j))
        distance_J = distance_J_letters + distance_J_words
        if index_i != index_j and distance_J <= 0.3215:
            col_list.append(index_j)
    if len(col_list) > 0:
        row_list.append(index_i)
        row_list.append(col_list)
    return(row_list)

#row_list = detect_near_duplicates(0, data)
#print(row_list)

list_of_lists = []
index_i = -1
for i in data:
    index_i += 1
    index_j = -1
    iteration_start = time.perf_counter()
    row_list = detect_near_duplicates(index_i, data)
    list_of_lists.append(row_list)
    row_number = index_i+1
    iteration_end = time.perf_counter()
    iteration_total = (iteration_end - iteration_start)
    percent_complete = (row_number)/len(data)
    status= "Row {} finished in {} seconds...{}% complete".format(row_number, iteration_total, percent_complete)
    print(status)

#https://towardsdatascience.com/a-laymans-guide-to-fuzzy-document-deduplication-a3b3cf9a05a7   


#create a list of duplicate vendor_names and their difference scores
list_of_lists = []
index_i = -1
for i in data:
    index_i += 1
    index_j = -1
    iteration_start = time.perf_counter()    
    for j in data:
        index_j += 1
        tokens_i = nltk.word_tokenize(i)
        tokens_j = nltk.word_tokenize(j)
        distance_J_letters = nltk.jaccard_distance(set(i), set(j))
        distance_J_words = nltk.jaccard_distance(set(tokens_i), set(tokens_j))
        distance_J = distance_J_letters + distance_J_words
        if index_i != index_j and distance_J <= 0.3215:
            min_index = min(index_i, index_j)
            max_index = max(index_i, index_j)
            temp_list = [min_index, max_index, distance_J]
            #list_of_lists.append(temp_list)
            if temp_list not in list_of_lists:
                list_of_lists.append(temp_list)
    row_number = index_i+1
    iteration_end = time.perf_counter()
    iteration_total = (iteration_end - iteration_start)
    percent_complete = (row_number)/len(data)
    status= "Row {} finished in {} seconds...{}% complete".format(row_number, iteration_total, percent_complete)
    print(status)

#print(list_of_lists)
'''
#from list of duplicates, measure name_and_street string similarity
for i in list_of_lists:
    temp_list = i
    min_index = temp_list[0]
    max_index = temp_list[1]
    sentence01 = vendors_df['VENDOR_NAME_AND_STREET'][max_index].upper()
    sentence02 = vendors_df['VENDOR_NAME_AND_STREET'][min_index].upper()
    distance_L = nltk.edit_distance(sentence01, sentence02)
    #distance_J = nltk.jaccard_distance(set(sentence01), set(sentence02))
    if distance_L >=5:
        address_match = False
    else:
        address_match = True
    i.append(address_match)
    
    
    #temp_dict = { 'VENDOR_KEY_01': vendors_df['VENDOR_KEY'][index_i], 'VENDOR_KEY_02': vendors_df['VENDOR_KEY'][index_j], 'VENDOR_PARENT_NAME': vendors_df['VENDOR_NAME'][parent_name], 'LEVENSHTEIN': distance_L, 'JACCARD': distance_J}
    #list_of_duplicates.append(temp_dict)
'''

#for duplicates, update dataframe parent_key field with earliest parent vendor_key value
for i in list_of_lists:
    temp_list = i
    min_index = temp_list[0]
    max_index = temp_list[1]
    parent_id = my_df['VENDOR_KEY'][min_index]
    parent_key_loc = my_df['PARENT_KEY'][max_index]
    if parent_key_loc == '' or parent_id < parent_key_loc :
        vendors_df2.at[max_index, 'PARENT_KEY'] = parent_id
    print(parent_id)

vendors_df.head

#export dataframe
target_file = "Vendor_Clean.csv"
target_path = path+target_file
my_df.to_csv(target_path, index = False)