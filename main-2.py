from bs4 import BeautifulSoup
import requests

req = requests.get('https://www.eurekaca.gov/744/Current-Projects')
soup = BeautifulSoup(req.content, 'html.parser')

r = soup.findAll('div', class_='widget editor pageStyles narrow')
for i in r:
    y = i.text
    print(y)
