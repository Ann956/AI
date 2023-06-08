import requests
from bs4 import BeautifulSoup
url = f'https://pedia.cloud.edu.tw/Entry/Detail?title={word}&search={word}#searchL'
html = requests.get( url )
bs = BeautifulSoup(html.text,'lxml')
data = bs.find('span', class_='withoutRefLink')
data.text
