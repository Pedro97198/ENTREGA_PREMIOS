import requests
from bs4 import BeautifulSoup
import urllib
from urllib.parse import urlparse

#Define the request logic
def getdata(url):
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}

  response = requests.get(url,
                          headers=headers)
  parsed_url = urlparse(url)
  domain = parsed_url.netloc

  return response.text, domain

# URL we are goint to work with 
# url = 'https://www.supercoloring.com/es/dibujos-para-colorear/ciencia-y-educacion/alfabetos/asl-alphabet-american-sign-language'#/robots.txt '
url = 'https://fundacioncnse-dilse.org/?buscar='
htmldata = getdata(url)[0]

#Initializating BeautifulSoup
soup = BeautifulSoup(htmldata, 'html.parser')

#Making the scraping logic
it = 0
for item in soup.find_all('img'):
  print(item['src'], type(item['src']))
  print(item['src'][-3:], type(item['src'][-3:]))
  if len(item['src']) > 4:
    if item['src'][:4] =='http':
        urllib.request.urlretrieve(item['src'], item['src'].split("/")[-1])
        it += 1
    elif item['src'][0] =='/':
        imageUrl = 'https://' + getdata(url)[1] + item['src']
        urllib.request.urlretrieve(imageUrl, item['src'].split("/")[-1])
        it += 1
    elif item['src'].startswith('img/'):
        urllib.request.urlretrieve(url + item['src'], item['src'].split("/")[-1])
        it += 1

  else:
    #Tipical "No hay ná" situation 
    print('No hay ná')

