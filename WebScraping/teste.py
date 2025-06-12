import requests
from bs4 import BeautifulSoup
import pandas as pd

dados = []

url_https = "https://www.alura.com.br/artigos/conhecendo-o-modelo-osi?srsltid=AfmBOopOJElOXWM5m2Q9kmpHSpRxzZXJPTxjXYVgKOj4eZ-f_mYOOeUy"
res_https = requests.get(url_https)
soup_https = BeautifulSoup(res_https.content, "html.parser")


for tag in soup_https.find_all(["h1", "h2", "p"]):
    texto = tag.get_text(strip=True)
    if texto:
        dados.append({"site": "Alura (HTTPS)", "conteudo": texto})

df = pd.DataFrame(dados)
print(df)

url_http = "http://httpforever.com/"
res_http = requests.get(url_http)
soup_http = BeautifulSoup(res_http.content, "html.parser")

for tag in soup_http.find_all(["h2", "p"]):
    texto = tag.get_text(strip=True)
    if texto:
        dados.append({"site": "HTTPForever (HTTP)", "conteudo": texto})

df = pd.DataFrame(dados)
print(df)

# df.to_csv("topicos_https_http.csv", index=False)