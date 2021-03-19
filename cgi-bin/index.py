#!shebang here
# -*- coding: utf-8 -*-
import cgi
import requests

CLIENT_ID = ''
CLIENT_SECRET = ''

GRANT_TYPE = 'client_credentials'
TOKEN_URL = 'https://accounts.spotify.com/api/token'

body_params = {'grant_type': GRANT_TYPE}
auth = requests.post(TOKEN_URL, data=body_params, auth=(CLIENT_ID, CLIENT_SECRET)).json()
header_params = {'Authorization': 'Bearer {}'.format(auth['access_token'])}

ENDPOINT = 'https://api.spotify.com/v1/artists/'
html_main_content = ""

artist_key = [
    '5FwydyGVcsQllnM4xM6jw4', # american football
    '5vfSFPrDPPBGExVLldEDOB', # enemies
    '5uvVjg5SwNjvNE4w7HlGJC', # vasudeva
    '15apg2MS107wZD0LvXnkMw', # tangled hair
    '7663vNncj70kCkfsi5eMNf', # clever girl
    '4GkcDsTHzavL8eDEsEaC1D', # last days of april
    '1FVOt1XlpnaCueBolWF92k', # floral
    '69SoLkfU8ctU5vxrvsA0FT', # closure.
    '05MlomiA9La0OiNIAGqECk', # delta sleep
    '6GAoXkyadLFOLLkZrHWlOR', # tide/edit
    '2PxyBZt0Dgp57wZUHkzKmW', # football etc
    '3qu0nHytyZet7JFUe2Afow', # via luna
    '46iJ1VD4HKFnqjISGqlZkV', # covet
    '5luRIEhyaVB12mabNujZHx', # hikes 
    '7zRVN0utSt9TFWfGPTYOkQ', # Halfsleep
    '0rpKM0MniNkXM1SLSglYUZ', # toe
    '2J2ulUwLz2ItsDwB5V4LxU', # stereo type
    '0nwTdEUuG7c1M3kR9CIIxm', # syroup16g
    '6VIUbb5oBJPnm2gcYMFBUR', # jyocho
    '7j5EuAboK71i18fZONW3Ys', # cetow
    '5IKKS7LhpdlmMwqIagqf3f', # tricot
    '0TF6B1cp2QZXLE0NjhTMT9', # lite
    '0jE8JREE3hzVFAOnbBkK0r', # rega
    '2DZe9zw4ZNgEFPA8vRMade' # 宇宙コンビニ
]

for current_artist_key in artist_key:
    current_endpoint = ENDPOINT + current_artist_key
    res = requests.get(current_endpoint, headers=header_params)

    artist_name = res.json()['name']
    artist_image = res.json()['images'][0]['url']

    current_grid_content = '''
        <div class="artist-effect">
            <div class="grid-item">
                <form action="/cgi-bin/artist.py" method="POST">
                    <input type="hidden" name="key" value="%s" >
                    <input class="img-cover" type="image" src="%s" alt="send">
                    <div class="mask">        
                        <div class="caption"><h2>%s</h2></div>
                    </div>
                </form>
            </div>  
        </div> 
    '''% (current_artist_key, artist_image, artist_name)

    html_main_content += current_grid_content + '\n'

content_1 = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Takumi Influenced</title>


<link rel="stylesheet" href="https://unpkg.com/sanitize.css">
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho+B1&family=Source+Code+Pro:ital,wght@0,300;1,300&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/style.min.css">
</head>
<body>
<header>
<div class="header-text">
<h1 class="header-title">Takumi Influenced</h1>
<p class="header-description">
twinkle riff,<br>
irregular time signature,<br>
and tapping.<br>
that has makes me.
</p>
</div>
<img src="../img/header-background.jpg" alt="background-image">
</header>

<main class="grid">
"""

content_2 = """
</main>

<footer class="footer">
<h1 class="footer-title"><a href="index.py">Takumi Influenced</a></h1>

<p class="footer-copyright">© 2021 takumi kamihara</p>
</footer>

</body>
</html>
"""

form = cgi.FieldStorage()

print('Content-Type: text/html; charset=UTF-8\n')
print(content_1)
print(html_main_content)
print(content_2)
