import pandas as pd

#declare directory
path = "../../Tables/"

#from directory, select csv to import
target_file = "Vendor.csv"
target_path = path + target_file

#import csv and create dataframe
df = pd.read_csv(target_path, encoding='ISO-8859-1')

df2 = df[0:10]

#remove comma delimter within string

def replace_char_in_column(df, column, old_char, new_char):
    df[column] = df[column].str.replace(old_char, new_char)
    return df[column]

my_column = 'VENDOR_ADDRESS'
old_char = ','
new_char = ';' 

replace_char_in_column(df, my_column, old_char, new_char)

    
#export csv with utf-8 encoding
target_file = "Vendor_utf8.csv"
target_path = path + target_file

df.to_csv(target_path, encoding='utf-8', index=False)