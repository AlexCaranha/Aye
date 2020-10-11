# pip install PyDictionary

from PyDictionary import PyDictionary
import goslate

gs = goslate.Goslate()
languages = gs.get_languages()
print(f"línguas: {languages}")

dictionary=PyDictionary()

# print(dictionary.meaning("indentation"))
traducao = dictionary.translate("Range",'pt')
significado = dictionary.meaning(traducao)
print(significado)
