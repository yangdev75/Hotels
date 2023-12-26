from utils import controls

import os
import requests
from bs4 import BeautifulSoup as bs
import wget
import datetime
import locale

import pprint

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')


hotel_url = 'https://www.data.gouv.fr/fr/datasets/hebergements-collectifs-classes-en-france/'
file_root_name = 'hotels_'


if "data" not in os.listdir():
    os.mkdir("data")

# if controls.is_url_OK(hotel_url):
#     response=requests.get(hotel_url)
#     soup = bs(response.content, features='html.parser')

#     last_update = soup.find("p", attrs={'class': 'fr-text--sm fr-mt-0 fr-mb-3v'}).text.strip()
#     last_update = datetime.datetime.strptime(last_update, "%d %B %Y")
#     print (f"last update is {last_update.date()} (datetime format)")
#     filename = file_root_name + last_update.date().strftime("%Y_%m_%d") +".csv"
#     print(filename)
#     if not os.listdir("data"):
#         links=soup.find_all("a", attrs={'title': 'Télécharger le fichier'})
#         print (links[1])
#         data_link = links[1]['href']
#         wget.download(data_link, out=f"data/{filename}")
#     else:
#         file_breakdown = os.listdir("data")[0].split("_")
#         file_year=file_breakdown[1]
#         file_month=file_breakdown[2]
#         file_day=file_breakdown[-1].split('.')[0]
#         filedate = datetime.datetime.strptime(f"{file_day} {file_month} {file_year}", "%d %m %Y")
#         print(f"current file date is {filedate.date()}")
#         if last_update > filedate:
#             print('delete current file')
#             file_path = os.path.join("data", os.listdir("data")[0])
#             os.remove(file_path)
#             links=soup.find_all("a", attrs={'title': 'Télécharger le fichier'})
#             data_link = links[1]['href']
#             print('DL new file')
#             wget.download(data_link, out=f"data/{filename}")

# else:
#     print(f"can't access {hotel_url}")



url = 'https://adresse.data.gouv.fr'
root="/data/ban/adresses/latest/csv/"
adresse_url = url+root

if "addresses" not in os.listdir("data"):
    os.mkdir("data/addresses")


if controls.is_url_OK(hotel_url):
    response = requests.get(adresse_url)
    soup = bs(response.content, features="html.parser")

    if not os.listdir("data/addresses"):
        links = soup.find_all("a",attrs={'class': 'jsx-2832390685'})
        
        # links = links[25:33]
        links = links[-5:]
        for a in links:
            filename = a["href"]
            print(filename)

            if (root in filename):
                print("aaa")
                link = url + filename
                print(f"link: {link}")

                # response = requests.head(link)
                # print(response.headers)
                # last_modified = response.headers.get('Last-Modified')
                # print(last_modified)

                if controls.is_gz_file_not_empty(link):
                    wget.download(link,out=f"data/addresses/")
                    last_update=a.find("span", attrs={'class': 'jsx-2832390685 explorer-link-date'}).text
                    last_update = datetime.datetime.strptime(last_update, "%d/%m/%Y")
                    print(last_update.date())

else:
    print(f"can't access {hotel_url}")
