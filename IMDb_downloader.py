import random
import requests
from bs4 import BeautifulSoup
import re

def download_from(site):
    user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/56.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.1.2 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/15.3 Mobile/15E148 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/537.36"
]

    headers = {'User-Agent': random.choice(user_agents)}
    response = requests.get(site, headers=headers)      # response es la respuesta al enviar una solicitud HTTP.
    if response.status_code != 200:
        print('IMDb access error', response.status_code)
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')  # Analiza el contenido HTML de la página.
    images = soup.find_all('img')                       # Resultado de buscar todas las etiquetas <img> en soup.

    description = images[2].get('alt', 'frame')         # Obtención de la descripción textual alternativa de la imagen.
    description = re.sub(r'[\\/:*?"<>|]', '', description)
    picture_url = images[2].get('src')                  # Obtención del atributo src (source).
    pic_response = requests.get(picture_url)
    if pic_response.status_code != 200:
        print('Download failed', pic_response.status_code)
        return None

    # type(pic_response.content)                        # Tipo del contenido de pic_response. (bytes)
    with open(description+'.jpg', 'wb') as file:
        file.write(pic_response.content)
        print('Successfully downloaded')

url = input('Insert URL: ')                             # Pide la URL.
# url = 'https://www.imdb.com/title/tt5040012/mediaviewer/rm2594863105/'
download_from(url)
