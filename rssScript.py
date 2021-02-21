import feedparser
import requests
import xml.etree.ElementTree as eltree

expansion = 'https://e00-expansion.uecdn.es/rss/empresasdigitech.xml'
economista ='https://www.eleconomista.es/rss/rss-empresas.php'
cincodias ='https://cincodias.elpais.com/seccion/rss/companias/'
confidencial = 'https://rss.elconfidencial.com/empresas/'

response = requests.get(confidencial)
tree = eltree.fromstring(response.content)
items = tree.findall('channel/item')


if items == []:
    feed = feedparser.parse(confidencial)
    items = feed.entries

itemsFiltrados = []

for item in items:

    part = item.title#formato para atom

    descripcion = item.findtext('description')#formato para rss

    if 'Telefónica' in part or 'Caixa' in part:
        itemsFiltrados.append(item)

print(itemsFiltrados)


def getXML(url, atom):

    itemsFiltrados = []


    try:
        response = requests.get(url)

        tree = eltree.fromstring(response.content)

        items = tree.findall('channel/item')

        for item in items:
            categories = item.findall('category')
            for category in categories:
                if 'Telefónica' in category.text:
                    itemsFiltrados.append(item)
    except:
        pass

    return itemsFiltrados


