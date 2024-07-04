import requests

url = 'https://google.com/'

response = requests.get(url)

with open('index.html', 'w') as f:
    f.write(response.text)




# try:
#     response = requests.get(url)
#     response.raise_for_status()
#     print(response.status_code)
# except requests.exceptions.HTTPError as errh:
#     print('htpp error: ', errh)
# except requests.exceptions.ConnectionError as errc:
#     print('error connection: ', errc)
# except requests.exceptions.Timeout as errt:
#     print('Time out error: ', errt)
# except requests.exceptions.RequestException as err:
#     print('OOops something else', err)