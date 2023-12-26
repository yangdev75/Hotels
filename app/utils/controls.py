import requests

def is_url_OK(url:str):
    response=requests.get(url)
    return response.status_code == 200


def is_gz_file_not_empty(url:str):
    response = requests.head(url)
    # print(response.headers)
    content_length = int(response.headers.get('Content-Length'))
    print(content_length)
    # strangely, content-length is equal 20 when empty
    return content_length > 20
