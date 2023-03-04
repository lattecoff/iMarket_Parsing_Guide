# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup

list_cards_url = []

for num_page in range(1, 2):
    webaddr = f"https://scrapingclub.com/exercise/list_basic/?page={num_page}"
    webpage = requests.get(webaddr)

    # Копируем html-код страницы в переменную webpage_html_code.
    webpage_html_code = BeautifulSoup(webpage.text, "lxml")

    # Ищем все div-блоки с определенным классом и копируем их в list_product_cards
    list_product_cards = webpage_html_code.find_all("div", class_ = "col-lg-4 col-md-6 mb-4")

    # Далее проходимся по карточкам товаров и выдераем ссылки на их.
    # С помощью метода find() находим нужный тег.
    # С помощью метода get() находим нужный аттрибут.
    for card in list_product_cards:
        card_url = "https://scrapingclub.com" + card.find("a").get("href")
        list_cards_url.append(card_url)


for card_url in list_cards_url:
    # По адресу карточки, копируем ее html-код.
    card = requests.get(card_url)
    card_html_code = BeautifulSoup(card.text, "lxml")

    # И забираем все информацию о товаре.
    product_card_info = card_html_code.find("div", class_="card mt-4 my-4")

    # Разбираем информацию карточки на категории.
    product_name = product_card_info.find("h3", class_ = "card-title").text
    product_price = product_card_info.find("h4").text
    product_text = product_card_info.find("p", class_ = "card-text").text
    product_image = product_card_info.find("img", class_ = "card-img-top img-fluid").get("src")

    print(product_name + "\n" + product_price + "\n" + product_text + "\n\n")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
