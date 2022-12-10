import pandas as pd
import time
from mlxtend.preprocessing import TransactionEncoder

''' READ IN AND FORMAT DATA '''

#read in vendors.csv as dataframe
path = "../../ToUpload/"
target_file = "PO_master.csv"
target_path = path+target_file
orders_df = pd.read_csv(target_path, encoding='ISO-8859-1', low_memory=False)

#filter/format df for transformation
orders_df = orders_df[orders_df['TOTAL_COST'] > 0]
orders_df = orders_df[orders_df['DATE_ORDER'] > '2018-12-31']
orders_df.sort_values(by='DATE_ORDER', inplace=True, ascending=False)

#slice dataframe by key column
key_column = 'AGENCY_KEY'
values_column = 'NIGP_KEY'

orders_df = pd.DataFrame(orders_df, columns = [key_column, values_column])

''' DECLARE FUNCTIONS '''

#calculate total_time
def print_total_time(start_time, end_time, total_row_count):
    total_time = (end_time - start_time)/60
    output_str = "{} rows in {} minutes".format(total_row_count, total_time)
    return (output_str)

#export dataframe
def export_dataframe(dataframe, path, filename):
    target_path = path + filename
    lol_df.to_csv(target_path, index = False)
    return

# create list_of_lists of all transation pairs
def list_unique_ids (dataframe, key_column):
    my_column = dataframe[key_column]
    my_list = list(my_column.unique())
    return(my_list)

#unique_key_ids = list_unique_ids(mydf, key_column)

#split data into (n) number of chunks
def chunk_data(my_list, num_of_clusters):
    num_of_clusters = 5
    len_list = len(my_list)
    chunk_size = (len_list//num_of_clusters)+1
    chunked_list = [my_list[i:i+chunk_size] for i in range(0, len(my_list), chunk_size)]
    return(chunked_list)

#list_id_chunks = chunk_data(unique_key_ids, 5)
#chunk = list_id_chunks[0]

#create a list_of_list of all transactions with more than one product
def orders_have_products(chunk, dataframe, key_column, values_column):
    row_count = 0
    total_row_count = 0
    iteration_count = 0
    start_time = time.perf_counter()
    iteration_time = time.perf_counter()
    list_of_lists = []
    for key in chunk:
        temp_df = dataframe[dataframe[key_column] == key]
        temp_df = temp_df.set_index(key_column)
        temp_list = list(temp_df[values_column].unique())  
        if len(temp_list) > 1:
            list_of_lists.append(temp_list)
        row_count += 1
        total_row_count += 1
        if row_count == 100:
            iteration_count += 1
            mid_time = time.perf_counter()
            my_string = print_total_time(iteration_time, mid_time, row_count)
            print(str(iteration_count) + " - " + my_string)
            row_count = 0
            iteration_time = time.perf_counter()
    end_time = time.perf_counter()
    my_string = print_total_time(start_time, end_time, total_row_count)
    print("\n" + my_string)
    return(list_of_lists)

def create_transactions_lol(list_id_chunks, dataframe, key_column, values_column):
    transactions_lol = []
    iteration_count = 0
    for i in list_id_chunks:
        iteration_count += 1
        df_filtered = dataframe[dataframe[key_column].isin(i)]
        my_string = '\n' + 'Chunk #{} created...'.format(iteration_count)
        print(my_string)
        temp_lol = orders_have_products(i, df_filtered, key_column, values_column)        
        for l in temp_lol:
            transactions_lol.append(l)
        my_string = '\n' + 'Chunk #{} completed...'.format(iteration_count)
        print(my_string)
    return (transactions_lol)

#transactions_lol = create_transactions_lol(list_id_chunks, mydf, key_column, values_column)

#transform lol into matrix using one hot encoding
def transform_lol_to_matrix(list_of_lists):
    one_hot_transformer = TransactionEncoder()
    df_transform = one_hot_transformer.fit_transform(list_of_lists)
    df = pd.DataFrame(df_transform,columns=one_hot_transformer.columns_)
    return(df)

''' CREATE A LIST-OF-LISTS OF ALL TRANSACTIONS WITH MULTIPLE PRODUCTS''' 

mydf = orders_df
#mydf = orders_df[0:100000]

unique_key_ids = list_unique_ids(mydf, key_column)

list_id_chunks = chunk_data(unique_key_ids, 5)

transactions_lol = create_transactions_lol(list_id_chunks, mydf, key_column, values_column)

print (transactions_lol)

#export dataframe
def export_dataframe(dataframe, path, filename):
    target_path = path + filename
    dataframe.to_csv(target_path, index = False)
    return

transactions_df = pd.DataFrame(transactions_lol)
path = "../ToUpload/Outputs/"
target_file = "ProductsByAgency_LoL.csv"
export_dataframe(transactions_df, path, target_file)

''' FORMAT TRANSACTIONS_LOL INTO A MATRIX '''

products_matrix = transform_lol_to_matrix(transactions_lol)

#export orders_product_matrix
path = "../ToUpload/Outputs/"
target_file = "Agency_Product_Matrix.csv"
export_dataframe(products_matrix, path, target_file)


#https://medium.com/mlearning-ai/market-basket-analysis-step-by-step-coding-cd13ce1f8de9 