import requests
from bs4 import BeautifulSoup
def read( word ):
    url = f'https://dict.idioms.moe.edu.tw/idiomList.jsp?idiom={word}&qMd=0&qTp=1&qTp=2#searchL'
    
    html = requests.get( url )
    bs = BeautifulSoup(html.text,'lxml')
    data = bs.find('table', id='searchL')
   
    try:
        row = data.find_all('tr')[2]
        chinese = row.find('cr').text
        phones = row.find_all('code')
        phone = [e.text for e in phones]
        s = " ".join( phone )
        # s = row.find('sub')
        print( chinese+ s )
    except:
        print( '查無此成語' )
