import json
from pprint import pprint
import requests

if __name__ == '__main__':
    headers = {
        'Authorization': 'Bearer {{ YOUR_VALUE }}',
        'Content-Type': 'application/json',
    }
    response = requests.get('https://api.spotify.com/v1/playlists/{{ YOUR_VALUE }}/tracks?market=US&fields=%20items(track(name)%2Ctrack(album(artists(id))))', headers=headers).json()
#    pprint(type(response))
#    pprint(response['items'])
    for x in response['items']:
         #pprint (x['track']['name'])
         song = x['track']['name']
         #pprint(x['track']['album']['artists'][0]['name'])
         artist = x['track']['album']['artists'][0]['name']
         pprint (str(song) + ': ' + str(artist))
