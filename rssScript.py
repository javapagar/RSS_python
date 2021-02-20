import pandas as pd
import requests as request
import xml.etree.ElementTree as xmlET

url = 'https://e00-expansion.uecdn.es/rss/empresasdigitech.xml'

portada = xmlET.parse(request.get(url, 'rb'))
root = portada.getroot()

print(root)



