import requests
from bs4 import BeautifulSoup
import pandas as pd

def peganoticia():
    cnn = 'https://www.cnnbrasil.com.br/'
    response = requests.get(cnn, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.content, 'html.parser')

    noticias = []

    for bagulho in soup.find_all(['a', 'h2', 'h3']):
        texto = bagulho.get_text(strip=True)
        if texto and len(texto) > 30 and texto not in noticias:
            noticias.append(texto)

    if noticias:
        print("lista de notícias da página principal:")
        for i, noticia in enumerate(noticias, 1):
            print(f"{i}. {noticia}")

    return noticias
peganoticia()
