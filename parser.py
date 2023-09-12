import flask, requests
from pprint import pprint
import psycopg2
import json
# URL = 'https://catalog.wb.ru/catalog/toys5/catalog?appType=1&cat=9541&curr=rub&dest=-1257786&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,1,31,66,110,48,22,71,114&sort=popular&spp=33'
# all categories (https://static-basket-01.wb.ru/vol0/data/main-menu-ru-ru-v2.json)

class Info:
    """class get brands information from WB"""
    def __init__(self, url):
        self.url = url
        self.response = None
        self.result = dict()
    def get_response(self):
        self.response = requests.get(self.url).json()
        for info in self.response['data']['products']:
            if info['brand'] in self.result:
                self.result[info['brand']].append(
                    {'id': info['id'], 'name': info['name'], 'price': info['salePriceU'] // 100,
                     'raiting': info['rating'], 'feedback': info['feedbacks']})
            else:
                self.result[info['brand']] = [
                    {'id': info['id'], 'name': info['name'], 'price': info['salePriceU'] // 100,
                     'raiting': info['rating'], 'feedback': info['feedbacks']}]
            self.db_update(company_name=info['brand'],product_id=info['id'],item_name=info['name'],price=info['salePriceU'] // 100,raiting=info['rating'],feedback=info['feedbacks'])
    def connect_db(self):
        self.conn = psycopg2.connect(database="parsing_wb_antistress", user="postgres",
                                password="1234567890", host="localhost", port=5432)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
    def db_update(self, **kwargs):
        self.connect_db()
        self.cur.execute(
            f"INSERT INTO public.parsing_wb_antistress (company_name, product_id, item_name, price, raiting, feedback) VALUES('{str(kwargs['company_name'])}', '{int(kwargs['product_id'])}', '{str(kwargs['item_name'])}', '{int(kwargs['price'])}', '{int(kwargs['raiting'])}', '{kwargs['feedback']}');")
        self.cur.execute('select * from parsing_wb_antistress')
        print(self.cur.fetchall())
        return None

    def get_info(self):
        self.get_response()
        return self.result
    def __len__(self):
        return len(self.result)

URLS = ['https://catalog.wb.ru/catalog/toys5/catalog?appType=1&cat=9541&curr=rub&dest=-1257786&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,1,31,66,110,48,22,71,114&sort=popular&spp=33']
antistress = Info(URLS[0])
pprint(antistress.get_info())
print(len(antistress.result))

