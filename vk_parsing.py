import os #для импорта токена
import vk_token #для импорта токена
import vk

api = vk.API(access_token=os.getenv('TOKEN'))
posts = api.wall.get(owner_id=-15755094, count=100,v=5.151) #15755094,20629724

for post in posts['items']:
    print(post['text'])