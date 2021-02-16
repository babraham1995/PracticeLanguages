from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'lxml')
page = BeautifulSoup(requests.get(url).text, "lxml")

input = input("enter file name: ")
open_file = open(input, 'w')

def printTitle():
    page = BeautifulSoup(requests.get(url).text, "lxml")
    for headlines in page.find_all('h2'):
        open_file.write(headlines.text)
        open_file.write('\n')
    

printTitle()
open_file.close()
