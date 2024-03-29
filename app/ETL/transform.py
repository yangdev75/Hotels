import pandas as pd
import polars as pl
import json
import os


def clean_hotel(hotels_path):
    with open('app/config/data_schemas.json', 'r') as schema_file:
        schema = json.load(schema_file)
        dtype_hotel = schema["hotels"]
        print(dtype_hotel)

    hotel_filename = os.listdir(hotels_path)[0]

    df_hotel = pd.read_csv(filepath_or_buffer=hotels_path+"/"+hotel_filename,
                            sep=";",
                            dtype=dtype_hotel,
                            na_values=["-", "non", "oui"])
    print(df_hotel.dtypes)

    size=len(df_hotel)
    print(f"dataframe length:{size}")

    accommodations_type = "HÔTEL DE TOURISME"
    columns_to_removes=["MENTION (villages de vacances)",
                        "CATÉGORIE",
                        "NOMBRE DE LOGEMENTS (villages de vacances)",
                        "TYPE DE SÉJOUR",
                        "NOMBRE D'EMPLACEMENTS",
                        "NOMBRE D'UNITES D'HABITATION (résidences de tourisme)",
                        "classement prorogé"]

    df_hotel_clean = df_hotel[df_hotel["TYPOLOGIE ÉTABLISSEMENT"]==accommodations_type].drop(columns=columns_to_removes)


    df_hotel_clean = df_hotel_clean.assign(CLASSEMENT=lambda x:x['CLASSEMENT'].str[:1])


    df_hotel_clean["DATE DE CLASSEMENT"]=pd.to_datetime(df_hotel_clean["DATE DE CLASSEMENT"], format="%d/%m/%Y")
    df_hotel_clean['CLASSEMENT'] = df_hotel_clean['CLASSEMENT'].str.replace('étoiles','stars')

    df_hotel_clean = df_hotel_clean.assign(
        YEAR=df_hotel_clean['DATE DE CLASSEMENT'].dt.year,
        MONTH=df_hotel_clean['DATE DE CLASSEMENT'].dt.month,
        DAY=df_hotel_clean['DATE DE CLASSEMENT'].dt.day
        )


    size=len(df_hotel_clean)
    print(f"dataframe length:{size}")
    pd.set_option('display.max_columns', None)

    # print(df_hotel_clean)
    print(df_hotel_clean.info())
    # print(df_hotel_clean)

def map_to_polars_dtype(dtype_str):
    dtype_mapping = {
        'str': pl.Utf8,
        "Float64": pl.Float64,
        # Add more mappings as needed
    }
    return dtype_mapping.get(dtype_str, pl.Utf8)
    
def clean_addresses(addresses_path):
    with open('app/config/data_schemas.json', 'r') as schema_file:
        schema = json.load(schema_file)
        dtype_addresses = schema["places"]
        print(dtype_addresses)

    print(dtype_addresses.items())
    

    dtype_addresses_pol = {col: map_to_polars_dtype(dtype_str) for col, dtype_str in dtype_addresses.items()}

    print(dtype_addresses_pol)
    dir = os.listdir(addresses_path)
    print(dir)

    add_folder = os.path.join(addresses_path, dir[0])
    addresses_filename = os.listdir(add_folder)[0]
    print(addresses_filename)

    df_adress = pl.scan_csv(add_folder + "/" + addresses_filename,
                            separator=";",
                            dtypes=dtype_addresses_pol)

   
    # df_adress = df_adress.collect()
    # print(len(df_adress))
    print(df_adress.describe())