from utils import controls, tools


import os
import requests
from bs4 import BeautifulSoup as bs
import wget
import datetime
import locale
import gzip
import shutil

import pprint

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')


# get hotels data at https://www.data.gouv.fr/fr/datasets/hebergements-collectifs-classes-en-france/
# ***********************************************

hotel_url = 'https://www.data.gouv.fr/fr/datasets/hebergements-collectifs-classes-en-france/'
file_root_name = 'hotels_'

if "data" not in os.listdir():
    os.mkdir("data")


hotels_path = "data/hotels"
if "hotels" not in os.listdir("data"):
    os.mkdir(hotels_path)

# if controls.is_url_OK(hotel_url):
#     response=requests.get(hotel_url)
#     soup = bs(response.content, features='html.parser')

#     # get date of last update to be used in the downloaded filename"
#     last_update = soup.find("p", attrs={'class': 'fr-text--sm fr-mt-0 fr-mb-3v'}).text.strip()
#     last_update = datetime.datetime.strptime(last_update, "%d %B %Y").date()
#     # print (f"last update is {last_update} (datetime format)\n")
#     filename = file_root_name + last_update.strftime("%Y_%m_%d") +".csv"
    
#     if not os.listdir(hotels_path): # if folder is empty
#         links=soup.find_all("a", attrs={'title': 'Télécharger le fichier'})
#         print (links[1]) # the 2nd element is the link we are looking for
#         data_link = links[1]['href']
#         wget.download(data_link, out=f"{hotels_path}/{filename}")
#         print(f"{filename} downloaded")
#     else:  # if folder is not empty : check whether the date of last update is more recent than the downloaded file
#         print('get date file')
#         filedate = tools.get_date_in_filename(hotels_path)
#         print(f"downloaded file dated from {filedate}")
#         if last_update >= filedate:
#             print('delete downloaded file')
#             tools.delete_files_or_folder(hotels_path)
#             links=soup.find_all("a", attrs={'title': 'Télécharger le fichier'})
#             data_link = links[1]['href']
#             print('DL new file')
#             wget.download(data_link, out=f"{hotels_path}/{filename}")

# else:
#     print(f"can't access {hotel_url}")



# get addresses at https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/
# ***********************************************

url = 'https://adresse.data.gouv.fr'
root="/data/ban/adresses/latest/csv/"
adresse_url = url+root


addresses_path = "data/addresses"
if "addresses" not in os.listdir("data"):
    os.mkdir(addresses_path)

french_addresses_path = addresses_path + "/adresses_fr/"
lieux_dits_path = addresses_path + "/lieux_dits/"
gz_folder_path = addresses_path + "/gz_folder/"
if "adresses_fr" not in os.listdir(addresses_path):
    os.mkdir(french_addresses_path)
if "lieux_dits" not in os.listdir(addresses_path):
    os.mkdir(lieux_dits_path)
if "gz_folder" not in os.listdir(addresses_path):
    os.mkdir(gz_folder_path)


if controls.is_url_OK(hotel_url):
    response = requests.get(adresse_url)
    soup = bs(response.content, features="html.parser")
    all_links = soup.find_all("a",attrs={'class': 'jsx-2832390685'})

    all_links = all_links[:3]
    # all_links = all_links[-5:]

    if not os.listdir(french_addresses_path):

        for link in all_links:
            filename = link["href"]

            if (root in filename):
                link_file = url + filename
                print(f"link: {link_file}")

                if controls.is_gz_file_not_empty(link_file):
                    wget.download(link_file,out=gz_folder_path)

                    brokendown_filename = filename.split('/')
                    name = brokendown_filename[-1]
                  
                    tools.extract_gz_file(gz_folder_path,name,link,french_addresses_path, lieux_dits_path)

                    print('delete gz file')
                    file_path = os.path.join(gz_folder_path)
                    tools.delete_files_or_folder(file_path)
        
        print('delete gz folder')
        os.rmdir(gz_folder_path)


    else:
        print('get date file')
        file_date = tools.get_date_in_filename(addresses_path)
        
        filename = all_links[0]["href"]
        print(filename)
        last_update=all_links[0].find("span", attrs={'class': 'jsx-2832390685 explorer-link-date'}).text
        last_update = datetime.datetime.strptime(last_update, "%d/%m/%Y")
        print(last_update.date())

        if file_date >= last_update.date():
            print("delete old files")
            tools.delete_files_or_folder(addresses_path)
            os.mkdir(french_addresses_path)
            os.mkdir(lieux_dits_path)
            os.mkdir(gz_folder_path)

            print("dl new files")


    # # print(response.headers)
    # last_modified = response.headers.get('Last-Modified')
    # print(f"links lastly modified on {last_modified}")
    # print(type(last_modified))



else:
    print(f"can't access {hotel_url}")
