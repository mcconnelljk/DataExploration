import pandas as pd 
import usaddress

#read in vendors.csv as dataframe
path = "../../Tables/"
target_file = "Vendor.csv"
target_path = path+target_file
vendors_df = pd.read_csv(target_path, encoding = 'utf-8-sig')
vendors_df = vendors_df.drop(['REGISTRATION_TYPE', 'VENDOR_ID', 'Order'], axis = 1)

#change default POS tag names
tag_mapping={
   'Recipient': 'recipient',
   'AddressNumber': 'address1',
   'AddressNumberPrefix': 'address1',
   'AddressNumberSuffix': 'address1',
   'StreetName': 'address1',
   'StreetNamePreDirectional': 'address1',
   'StreetNamePreModifier': 'address1',
   'StreetNamePreType': 'address1',
   'StreetNamePostDirectional': 'address1',
   'StreetNamePostModifier': 'address1',
   'StreetNamePostType': 'address1',
   'CornerOf': 'address1',
   'IntersectionSeparator': 'address1',
   'LandmarkName': 'address1',
   'USPSBoxGroupID': 'address1',
   'USPSBoxGroupType': 'address1',
   'USPSBoxID': 'address1',
   'USPSBoxType': 'address1',
   'BuildingName': 'address2',
   'OccupancyType': 'address2',
   'OccupancyIdentifier': 'address2',
   'SubaddressIdentifier': 'address2',
   'SubaddressType': 'address2',
   'PlaceName': 'city',
   'StateName': 'state',
   'ZipCode': 'zip_code',
}

#parse the addresses into a list of dictionaries - PARSE method
addresses_list = []
for index, row in vendors_df.iterrows():
    vendor_addr = usaddress.parse(row['VENDOR_ADDRESS'])
    vendor_addr_parts = []
    for i in vendor_addr:
        tuple_key = i[1]
        if tuple_key in tag_mapping.keys():
            tuple_key = tag_mapping[tuple_key]
        tuple_value = i[0]
        new_tuple = (tuple_key, tuple_value)
        vendor_addr_parts.append(new_tuple)
    vendor_key = ('VENDOR_KEY', str(row['VENDOR_KEY']))
    vendor_addr_parts.append(vendor_key)
    vendor_addr_dict = {}
    for key, value in vendor_addr_parts:
        if key in vendor_addr_dict:
            my_string = vendor_addr_dict[key] + " " + value
            vendor_addr_dict[key] = my_string.replace(",","").upper()
        else:
            temp_dict = {key: value.upper()}
            vendor_addr_dict.update(temp_dict)
    addresses_list.append(vendor_addr_dict)
#addresses_list[0]

#create a dataframe with selected vendor address columns
loc_df = pd.DataFrame({'VENDOR_KEY':[], 'VENDOR_STREET':[], 'VENDOR_UNIT':[], 'VENDOR_CITY':[], 'VENDOR_STATE':[], 'VENDOR_ZIP':[]})

#add list-of-dictionary values to dataframe as rows

#addresses_list2 = addresses_list[0:5]
for row in addresses_list:
    if 'VENDOR_KEY' in row:
        vendor_key = row['VENDOR_KEY']
    else:
        vendor_key = "NA"
    if 'address1' in row:
        vendor_street = str(row['address1']).upper()
    else:
        vendor_street = "NA"
    if 'address2' in row:
        vendor_unit = str(row['address2']).upper()
    else:
        vendor_unit = "NA"
    if 'city' in row:
        vendor_city = str(row['city']).replace(",","").upper()
    else:
        vendor_city = "NA"
    if 'state' in row:
        vendor_state = row['state'].upper()
    else:
        vendor_state = "NA"
    if 'zip_code' in row:
        vendor_zip = row['zip_code']
    else:
        vendor_zip = "NA"
    df_row = [vendor_key, vendor_street, vendor_unit, vendor_city, vendor_state, vendor_zip]
    loc_df.loc[len(loc_df)] = df_row

#loc_df.head()

#Export formated address dataframe as csv
target_file = "VendorHasAddress.csv"
target_path = path+target_file
loc_df.to_csv(target_path, index = False)

#fix bug where duplicates are introduced into loc_df