#!/opt/rh/rh-python38/root/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import requests

form = cgi.FieldStorage()
key = form.getfirst('key')

print('Content-Type: text/html; charset=UTF-8\n')

CLIENT_ID = ''
CLIENT_SECRET = ''
GRANT_TYPE = 'client_credentials'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
body_params = {'grant_type': GRANT_TYPE}

auth = requests.post(TOKEN_URL, data=body_params, auth=(CLIENT_ID, CLIENT_SECRET)).json()

header_params = {'Authorization': 'Bearer {}'.format(auth['access_token'])}
country_params = {'market':'jp'}

ENDPOINT = 'https://api.spotify.com/v1/artists/'

artist_endpoint = ENDPOINT + key 
toptrack_endpoint = ENDPOINT + key +  '/top-tracks'

res_artist = requests.get(artist_endpoint, headers=header_params)
res_toptrack = requests.get(toptrack_endpoint, headers=header_params, params=country_params)

name = res_artist.json()['name']
genre_arry = res_artist.json()['genre']
image = res_artist.json()['images'][0]['url']
artist_url = res_artist.json()['external_urls']['spotify']

toptrack_arry = []

for i in range(3):
    toptrack_arry.append(res_toptrack.json()['tracks'][i]['name'])

html_text = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Takumi Influenced</title>

    <link rel="stylesheet" href="https://unpkg.com/sanitize.css">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho+B1&family=Source+Code+Pro:ital,wght@0,300;1,300&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/artist.min.css">
</head>

<body>
    <main class="grid">
        <img class="grid-image" src="%s">
        <div class="grid-artist">
            <h1 class="grid-artist-title">%s</h1>
            <h2 class="grid-artist-genre-title">Genres:</h2>
                <ul class="grid-artist-genre">
                    <li>%s</li>
                </ul>
            <h2 class="grid-artist-toptracks">Toptracks:</h2>
            <ol class="grid-artist-toptracks-list">
                <li>%s</li>
                <li>%s</li>
                <li>%s</li>
            </ol>
            <a href="%s" target="_blank" class="bottun">Listen on Spotify</a>
            <a href="/cgi-bin/index.py" class="bottun-top">Back</a>
            </div>
        </div>
    </main>

    <footer class="footer">
        <h1 class="footer-title"><a href="index.py">Takumi Influenced</a></h1>
        <p class="footer-copyright">© 2021 takumi kamihara</p>
    </footer>

</body>
</html>
''' % (image, name, genre_arry[0], toptrack_arry[0], toptrack_arry[1], toptrack_arry[2], artist_url)

print(html_text)