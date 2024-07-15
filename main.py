from bs4 import BeautifulSoup
import requests

req = requests.get('https://www.ci.richmond.ca.us/1404/Major-Projects')
soup = BeautifulSoup(req.content, 'html.parser')
#s = soup.findAll('a', class_='Hyperlink')
#for i in s:
#    y = i.text.replace(' ','')
#    print(y)
r = soup.findAll('a', rel='noopener')
for i in r:
    y = i.text.replace(' ','')
    print(y)
links = []

for link in soup.find_all("a"): 
    href = link.get("href")
    if href and href.startswith("http"):
        links.append(href)
for link in links:
    nested_response = requests.get(link)
    nested_soup = BeautifulSoup(nested_response.content, "html.parser")
    
    # Extract data from nested page
    nested_data = nested_soup.find("div", id="moduleContent")
    if nested_data is not None:
        print(nested_data.text)


