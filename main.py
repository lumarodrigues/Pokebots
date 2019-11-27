import tweepy
import requests
import random
import time
from os import environ

API_KEY = environ['API_KEY']
API_SECRET = environ['API_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_SECRET = environ['ACCESS_SECRET']


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

interval = 60 * 60 * (1/2)  # tweet every 1/2 hour

while True:
    poke_number = random.randint(1, 809)
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_number}/')
    poke_name = r.json()['forms'][0]['name']

    words = []

    with open('adjectives.txt', 'r', encoding='utf-8') as archive:
        for line in archive:
            line = line.strip()
            words.append(line)

    i = random.randint(0, len(words))
    j = random.randint(0, len(words))
    api.update_status('Geralmente ' + poke_name.capitalize() + ' é ' + words[i] + '.' + ' Mas hoje está ' + words[j] + '.')
    print("Tweetou com sucesso!")
    time.sleep(interval)
