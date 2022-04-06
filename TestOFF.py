import requests
from bs4 import BeautifulSoup

'''the program is made to find out the minimum and maximum price, as well as counting goods by link'''

class Scraping:
print('Вставьте ссылку на товар: ') # ask to insert link

#link_catalog = {}  if have need find by name in dict!

def __init__(self):
    self.elem = input()  # input link

# def get_link(self):
#     for i in self.link_catalog:
#         if self.elem == i.lower().strip():   # if need to find by name in dict(name:link)
#             return self.link_catalog[i]

def scrap(self):  # parsing of site for find prices and output in terminal
    prise_list = []
    response = requests.get(self.elem) # if need to find by name in dict ( self.link_catalog)
    page = BeautifulSoup(response.text, 'lxml')
    for div in page.findAll('div', 'price'):  # for elements in class "price" we find prices.
                                              # if necessary, insert the necessary data for you for the place 'div' and 'price'
        price_item = ''
        for j in div.text:
            if j.isdigit():
                price_item += j
        price_item = int(price_item)
        prise_list.append(price_item)

    count = 0
    for i in range(len(prise_list)):  # cycle of count products
        count += 1
    print('Товаров по вашему запросу:', count)
    print('минимальная цена:', min(prise_list), '₽')
    print('максимальная цена:', max(prise_list), '₽')
g = Scraping()
g.scrap()