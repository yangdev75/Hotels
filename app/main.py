
from bs4 import BeautifulSoup as bs

import locale

import pandas as pd


import pprint


from ETL import extract
from ETL import transform

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')


hotels_path = "data/hotels"
# hotel_filename = extract.get_hotel_addresses(hotels_path)



addresses_path = "data/addresses"
extract.get_addresses(addresses_path)


# # get colums from hotels.csv
# # ***********************************************
# with open(hotels_path+"/"+hotel_filename) as csv_file:
#     csv_reader = csv.DictReader(csv_file, delimiter = ';')
#     dict_from_csv = dict(list(csv_reader)[0])
#     print (list(dict_from_csv.keys()))
#     pass

# print("df type without dict type\n")

# hotels_df = pd.read_csv(hotels_path+"/"+hotel_filename, sep=";")
# pd.set_option('display.max_columns', None)
# # print(hotels_df)
# print(hotels_df.describe())
# print(hotels_df.dtypes)


# print("\ndf type with dict type\n")
# with open('app/config/data_schemas.json', 'r') as schema_file:
#     schema = json.load(schema_file)
#     aa= schema["hotels"]
#     print(type(aa))
#     print(aa)


# df_hotel = pd.read_csv(filepath_or_buffer=hotels_path+"/"+hotel_filename,
#                         sep=";",
#                         dtype=aa,
#                         na_values=["-", "non", "oui"])
# print(df_hotel.dtypes)


print("main")
# transform.clean_hotel(hotels_path)