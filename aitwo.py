import requests
from bs4 import BeautifulSoup
import pandas as pd

ignorar = {''}

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

import os

def salvosim(novanoti, arquivo='noticias_cnn.csv'):
    if os.path.exists(arquivo):
        dfanti = pd.read_csv(arquivo)
        notianti = set(dfanti['Notícias'].tolist())
    else:
        notianti = set()

    unic = [noticia for noticia in novanoti if noticia not in notianti]

    if unic:
        dfnovo = pd.DataFrame({'Notícias': unic})
        dfreal = pd.concat([dfanti, dfnovo], ignore_index=True) if notianti else dfnovo
        dfreal.to_csv(arquivo, index=False, encoding='utf-8-sig')
        print(f"{len(unic)} novas notícias foram adicionadas ao '{arquivo}'.")
    else:
        print("nenhuma nova notícia foi adcionada.")

noticias = peganoticia()
salvosim(noticias)

def limpar_tokenizar(texto):
    palavras = re.findall(r'\b\w+\b', texto.lower())
    return [p for p in palavras if p not in ignorar]

#teste = limpar_tokenizar('noticias_cnn.csv')
#print(teste)

