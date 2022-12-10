import pandas as pd
import time
from mlxtend.frequent_patterns import apriori, association_rules

path = "../../ToUpload/Outputs/"
target_file = "Orders_Product_Matrix.csv"
target_path = path+target_file
orders_products_matrix = pd.read_csv(target_path, encoding = 'utf-8-sig')

df = apriori(orders_products_matrix, min_support = 0.05, use_colnames = True)
df.sort_values(['support'],ascending=False, inplace = True)
df_ar = association_rules(df, metric="lift", min_threshold=1)

path = "Output/"
target_file = "ProductAssociations.csv"
target_path = path + target_file

export_dataframe(df_ar, target_path, target_file)