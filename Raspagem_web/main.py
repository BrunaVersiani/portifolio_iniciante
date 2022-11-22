#Antes de começar baixei a biblioteca beautifuksoup4 (requests já baixado por padrão)

import requests
from bs4 import BeautifulSoup as bs

github_perfil = "https://github.com/raytechx"
req = requests.get(github_perfil)
scraper = bs(req.content, "html.parser")
foto_perfil = scraper.find("img", {"alt": "Avatar"})["src"]
print(foto_perfil)

'''Neste código eu simplesmente peguei a foto do meu perfil no github, mas essa ferramenta pode ser muito util para 
coletar dados de qualquer site na web.'''