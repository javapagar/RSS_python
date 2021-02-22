import feedparser
import requests
import xml.etree.ElementTree as eltree

def getReport(periodicos):
    report = ""
    for periodico in itemsFiltrados:

        report +=periodico[0] +"\n"

        for articulo in periodico[1]:
            if periodico[2]:
                report += articulo.title + "\n" + articulo.id + "\n"

            else:
                report +=articulo.findtext('title') + "\n" + articulo.findtext('link')+"\n"

        report +="\n"

    return report

def getXml(empresa, url):

    atom = False
    response = requests.get(url[1])
    tree = eltree.fromstring(response.content)

    items = tree.findall('channel/item')

    if items == []:
        feed = feedparser.parse(url[1])
        items = feed.entries
        atom = True

    itemsFiltrados = []


    for item in items:
        if atom:
            part = item.title  # formato para atom
        else:
            part = item.findtext('description')  # formato para rss

        if empresa in part:
            itemsFiltrados.append(item)

    tuplaItems = (url[0], itemsFiltrados, atom)

    return tuplaItems

empresa ="Telefónica"

expansion = ('Expansión','https://e00-expansion.uecdn.es/rss/empresasdigitech.xml')
economista = ('El Economista', 'https://www.eleconomista.es/rss/rss-empresas.php')
cincodias =('Cinco Dias', 'https://cincodias.elpais.com/seccion/rss/companias/')
confidencial = ('El Confidencial','https://rss.elconfidencial.com/empresas/')

lista = [expansion, economista, cincodias, confidencial]

itemsFiltrados = []

for url in lista:
    itemsFiltrados.append(getXml(empresa, url))

print(getReport(itemsFiltrados))



