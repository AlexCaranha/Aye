
import requests
from bs4 import BeautifulSoup

def get_definition(word):
    base_url = "https://api.dicionario-aberto.net/word/"
    url = base_url + word

    try:
        r = requests.get(url)

        if r.status_code != requests.codes.ok:
            return f"não foi possível consultar definição da palavra {word} no dicionário."        

        xml = r.json()[0]["xml"]
        bs = BeautifulSoup(xml, "xml")
        definition = bs.find("def").text
        return definition

    except:
        return f"não foi possível consultar a palavra {word} no dicionário."            

# definition = get_definition("corroboraram")
# print(f"corroborar: {definition}")
