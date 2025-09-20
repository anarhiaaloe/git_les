import requests
from bs4 import BeautifulSoup
import fake_useragent
from time import sleep


user = fake_useragent.UserAgent().random
header = {'User-Agent': user}
target_name_gpu = 'Рекомендуемая мощность блока питания'
target_name_block = 'Мощность'
target_name_block1 = 'Сертификат 80 PLUS'

def gpu():
    for count in range(1, 23): ## Всего 22 стр. Поменять на range(1, 23)
        sleep(3)
        url_gpu = f'https://novosibirsk.e2e4online.ru/catalog/videokarty-11/?page={count}'
        response = requests.get(url_gpu, headers=header)
        soup = BeautifulSoup(response.text, 'lxml') #html parser
        data = soup.find_all('div', class_='block-offer-item subcategory-new-offers__item-block')
        
        for i in data:
            card_url = 'https://novosibirsk.e2e4online.ru' + i.find('a').get('href')
            yield card_url
def array1():
    for card_url in gpu():
        response = requests.get(card_url, headers=header)
        soup = BeautifulSoup(response.text, 'lxml') #html parser
        data = soup.find_all('div', class_='e2e4-uikit-key-value-row offer-properties-new__property-item _preference-equal') ## Значения из "Характеристики"
        card_name = soup.find('h1', class_='offer-card-new__title')  ## Название видюхи
        
        for c in data:
            name_tag = c.find('span', class_='offer-properties-new__property-name-text')  ## Значения левого стобца
            value_tag = c.find('div', class_='offer-properties-new__property-value-item')  ## Значения из правого столбца
            if name_tag and name_tag.text.strip() == target_name_gpu:  ## Нужный левый столбец 'Рекомендуемая мощность блока питания'
                yield card_name.text.strip(), value_tag.text.strip()
                # print(card_name.text.strip())
                # print(value_tag.text.strip())
                # print()
                

    
def powerblock():
    for count in range(1, 46): ## Поменять на (1, 46)
        sleep(3)
        url_powerblock = f'https://novosibirsk.e2e4online.ru/catalog/bloki-pitaniya-6/?page={count}'
        response = requests.get(url_powerblock, headers=header)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all('div', class_='block-offer-item subcategory-new-offers__item-block')
        
        for i in data:
            card1_url = 'https://novosibirsk.e2e4online.ru' + i.find('a').get('href')
            yield card1_url
            
def array2():
    for card1_url in powerblock():
        response = requests.get(card1_url, headers = header)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all('div', class_='e2e4-uikit-key-value-row offer-properties-new__property-item _preference-equal')
        powerblock_name = soup.find('h1', class_='offer-card-new__title')
        
        for c in data:
            name_tag = c.find('span', class_='offer-properties-new__property-name-text')  ## Значения левого стобца
            value_tag = c.find('div', class_="offer-properties-new__property-value-item")  ## Значения из правого столбца
            if name_tag and name_tag.text.strip() == target_name_block:
                k = value_tag.text.strip()
            if name_tag and name_tag.text.strip() == target_name_block1:
                yield powerblock_name.text.strip(), k, value_tag.text.strip()
                
