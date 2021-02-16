import requests
from bs4 import BeautifulSoup

def drug_data():
    url = 'https://www.drugbank.ca/drugs/'

    while url:
        r = requests.get(url)
        soup = BeautifulSoup(r.text ,"lxml")

        url = soup.findAll('a', {'class': 'page-link', 'rel': 'next'})
        
        print(soup.find(class_='page-link', rel='next').text)

        print(soup.find(class_='name-value text-sm-center drug-name').text)

        if url:
            url = 'https://www.drugbank.ca' + url[0].get('href')
        else:
            break

drug_data()


# Solution, fucked
# import requests
# from bs4 import BeautifulSoup

# base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
# r = requests.get(base_url)
# soup = BeautifulSoup(r.text, 'lxml')

# all_p_cn_text_body = soup.select("div.parbase.cn_text > div.body > p")

# for elem in all_p_cn_text_body[7:]:
#   print(elem.text)

