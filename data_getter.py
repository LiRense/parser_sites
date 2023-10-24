import requests
from functools import lru_cache

def get_name(catalogues):
    new_catalog = {}
    for i in range(len(catalogues)):
        if 'childs' in catalogues[i].keys():
            a = len(catalogues[i]['childs'])
            new_podcatalog = []
            for j in range(a):
                 new_podcatalog.append(catalogues[i]['childs'][j]['name'])
            new_catalog[catalogues[i]['name']] = new_podcatalog
    return new_catalog

catalogues = requests.get('https://static-basket-01.wb.ru/vol0/data/main-menu-ru-ru-v2.json')
catalogues = catalogues.json()
new_catalog = get_name(catalogues)
