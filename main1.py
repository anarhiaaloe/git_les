import requests
from bs4 import BeautifulSoup
import fake_useragent
from time import sleep


user = fake_useragent.UserAgent().random
header = {'User-Agent': user}
list_card_url = []
target_name = 'Рекомендуемая мощность блока питания'

for count in range(1):
    sleep(3)
    url = f'https://novosibirsk.e2e4online.ru/catalog/videokarty-11/?page={count}'
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'lxml') #html parser
    data = soup.find_all('div', class_='block-offer-item subcategory-new-offers__item-block')
    
    for i in data:
        card_url = 'https://novosibirsk.e2e4online.ru' + i.find('a').get('href')
        list_card_url.append(card_url)

for card_url in list_card_url:
    response = requests.get(card_url, headers=header)
    soup = BeautifulSoup(response.text, 'lxml') #html parser
    data = soup.find_all('div', class_='e2e4-uikit-key-value-row offer-properties-new__property-item _preference-equal') ## Значения из "Характеристики"
    card_name = soup.find('h1', class_='offer-card-new__title')  ## Название видюхи
    
    for c in data:
        name_tag = c.find('span', class_='offer-properties-new__property-name-text')  ## Значения левого стобца
        value_tag = c.find('div', class_='offer-properties-new__property-value-item')  ## Значения из правого столбца
        if name_tag and name_tag.text.strip() == target_name:  ## Нужный левый столбец 'Рекомендуемая мощность блока питания'
            print(card_name.text.strip())
            print('Значение:', value_tag.text.strip())
            print()
            break
    
    