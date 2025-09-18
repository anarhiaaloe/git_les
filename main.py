import requests
from bs4 import BeautifulSoup
import fake_useragent

# # link = 'https://icanhazip.com/'
# # response = requests.get(link)
# # print(response.status_code)  #проверка статуса запроса (200 - значит правильный запрос, он дошёл до сервера и сервер на него ответил)
# print(response.text)




# link1 = 'https://browser-info.ru/'
# response1 = requests.get(link1).text
# with open('1.html', 'w', encoding='utf-8') as file:
#     file.write(response1) 


#========================================================================================================

# link1 = 'https://browser-info.ru/'
# response1 = requests.get(link1).text
# soup = BeautifulSoup(response1, 'lxml')
# block = soup.find('div', id = 'tool_padding')

# ### Проверяем джаваскрипт
# chek_js = block.find('div', id = 'javascript_check')
# status_js = chek_js.find_all('span')[1].text  ####так как в chek_js в строке встречается несколько span. мы вызываем find_all и берём необходимый по его индексу в строке [1]
# result_js = f'javascript {status_js}'
# ### проверяем флэш
# check_flash = block.find('div', id = 'flash_version')
# status_flash = check_flash.find_all('span')[1].text
# result_flash = f'flash {status_flash}'
# ### проверяем юзер агента
# check_user = block.find('div', id = 'user_agent').text
# result_user = f'{check_user}'  ### выводит User-agent: python-requests/2.32.5. Это имя юзер агента нужно подменить...

# print(result_js, result_flash, result_user, sep='\n')

#========================================================================================================

# user = fake_useragent.UserAgent().random

# header = {'user-agent': user}#-<<-----------------------------------------------
#                                       #                                         |
# link1 = 'https://browser-info.ru/'     #                                        |
# response1 = requests.get(link1, headers = header).text  ### подменяем user agent
# soup = BeautifulSoup(response1, 'lxml')
# block = soup.find('div', id = 'tool_padding')

# ### Проверяем джаваскрипт
# chek_js = block.find('div', id = 'javascript_check')
# status_js = chek_js.find_all('span')[1].text  ####так как в chek_js в строке встречается несколько span. мы вызываем find_all и берём необходимый по его индексу в строке [1]
# result_js = f'javascript {status_js}'
# ### проверяем флэш
# check_flash = block.find('div', id = 'flash_version')
# status_flash = check_flash.find_all('span')[1].text
# result_flash = f'flash {status_flash}'
# ### проверяем юзер агента
# check_user = block.find('div', id = 'user_agent').text
# result_user = f'{check_user}'  
# print(result_js, result_flash, result_user, sep='\n')

#========================================================================================================

############   Имя: samsmerd
############   Пароль: SLwtk0

# session = requests.Session()  ##это чтобы сессия сохраняляась и не приходилось логиниться каждый раз.
# ###                             позволяет записывать куки и продолжать с того места где остановились

# link = 'https://110km.ru/profile/'
# user = fake_useragent.UserAgent().random

# header = {
#     'user-agent': user
# }

# data = {
#     'login_user': 'qwerty@mail.ru',
#     'password_user': 'polovichok228'
# }

# response = session.post(link, data=data, headers=header).text ####все данные из запроса передаются в data, все заголовки помещаются в headers
# #                                                                 вместо response = requests.post используем response = session.post чтобы работать с куки

# profile_info = 'https://110km.ru/profile/?type=cars'
# profile_response = session.get(profile_info, headers=header).text
# print(profile_response)


# чёта нифига тут не получилось
#========================================================================================================

