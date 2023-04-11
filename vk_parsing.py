import os #для импорта токена
import vk_token #для импорта токена
import vk #импорт специализированной библиотеки для парсинга текста

api = vk.API(access_token=os.getenv('TOKEN'))  # адрес токена вк
posts = api.wall.get(owner_id=-15755094, count=100,v=5.151) #15755094,20629724
posts = api.wall.get(owner_id=-15755094, count=count,v=5.151) #15755094,20629724
#for post in posts['items']:
    #print(post['text'])

all_news = [] # переменная для добавления всех заголовков новостями
for post in posts['items']:
    all_news.append(post['text']) #добавляю все заголовки в один
    #возникла проблема с удалением лишних элементов

print(all_news)