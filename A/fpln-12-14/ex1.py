"""
Quais as Igrejas Românicas de Portugel?

1) wikipedia 

"""

import requests

url = "https://pt.wikipedia.org/w/api.php"
params = {
    "action": "query",
    "cmtitle": "Categoria:Igrejas_românicas_em_Portugal",
    "cmlimit": "150",
    "list": "categorymembers",
    "format": "json"
}
req = requests.get(url=url, params=params)
pages = req.json()
lista = pages['query']['categorymembers']

print(pages)
for page in lista:
    print (page)

