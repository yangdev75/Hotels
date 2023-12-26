import requests

def is_url_OK(url:str):
    response=requests.get(url)
    return response.status_code == 200
