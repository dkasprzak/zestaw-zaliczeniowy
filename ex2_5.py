import requests
import xml.etree.ElementTree as ET

url = "https://www.w3schools.com/xml/cd_catalog.xml"

response = requests.get(url)
response_content = response.content

root = ET.fromstring(response_content)

cd_list = []

for cd in root.findall('CD'):
    artist = cd.find('ARTIST').text
    title = cd.find('TITLE').text
    cd_list.append((artist, title))

for cd in cd_list:
    print(cd)
