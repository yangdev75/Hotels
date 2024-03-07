import pandas as pd
import json
import os


def clean_hotel(hotels_path):
    with open('app/config/data_schemas.json', 'r') as schema_file:
        schema = json.load(schema_file)
        dtype_hotel = schema["hotels"]
        print(type(dtype_hotel))
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
    df_hotel_clean = df_hotel[df_hotel["TYPOLOGIE ÉTABLISSEMENT"]==accommodations_type]

    df_hotel_clean = df_hotel_clean.assign(CLASSEMENT=lambda x:x['CLASSEMENT'].str[:1])


    size=len(df_hotel_clean)
    print(f"dataframe length:{size}")
    pd.set_option('display.max_columns', None)

    print(df_hotel_clean)


    