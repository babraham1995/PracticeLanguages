# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html)

def printTitle():
    page = BeautifulSoup(requests.get(url).text, "html")
    for headlines in page.find_all('h2'):
        print(headlines.text)

printTitle()


#solution
# base_url = 'http://www.nytimes.com'
# r = requests.get(base_url)
# soup = BeautifulSoup(r.text, 'lxml')

# for story_heading in soup.find_all('^h[1-6]$'): 
#     if story_heading.a: 
#         print(story_heading.a.text.replace("\n", " ").strip())
#     else: 
#         print(story_heading.contents[0].strip())