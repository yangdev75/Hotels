import requests
from bs4 import BeautifulSoup as bs
import wget

import pprint


# hotel_url = 'https://www.data.gouv.fr/fr/datasets/hebergements-collectifs-classes-en-france/'


# response=requests.get(hotel_url)
# print(response.status_code)

# soup = bs(response.content, features='html.parser')

# links=soup.find_all("a", attrs={'title': 'Télécharger le fichier'})
# print (links[1])
# data_link = links[1]['href']
# new_filename = 'hebergements-collectifs-classes-en-france.csv'


# wget.download(data_link, out=f"data/{new_filename}")
    



url = 'https://adresse.data.gouv.fr'
root="/data/ban/adresses/latest/csv/"
adresse_url = url+root
response = requests.get(adresse_url)
soup = bs(response.content, features="html.parser")
links = soup.find_all("a")
links = links[25:33]
for a in links:
    filename = a["href"]
    print(filename)

    if (root in filename):
        print("aaa")
        link = url + filename
        wget.download(link,out=f"data/addresses/")