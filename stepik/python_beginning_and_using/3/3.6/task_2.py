import requests
import json

client_id = 'your_id'
client_secret = 'your_secret'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

# инициируем запрос с заголовком

with open('dataset.txt', encoding='utf8') as f:
    s = [x.strip() for x in f.readlines()]

artists = []
for st in s:
    r = requests.get("https://api.artsy.net/api/artists/%s" % st, headers=headers)
    r.encoding = 'utf-8'
    r = json.loads(r.text)
    # разбираем ответ сервера
    artists.append(
        (r['birthday'], r['sortable_name'])
    )

for artist in sorted(artists, key=lambda x: (x[0], x[1])):
    print(artist[1])

