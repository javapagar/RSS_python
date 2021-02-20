import pandas as pd
import requests
import xml.etree.ElementTree as xmlET

url = 'https://e00-expansion.uecdn.es/rss/empresasdigitech.xml'

request = requests.get(url)

xmlPortada = xmlET.ElementTree(request.content)

root = xmlPortada.getroot()




