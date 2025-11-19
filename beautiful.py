# installed by pip requests and beautifulsoup4
import requests, bs4

res = requests.get('https://nostarch.com')

res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))

exampleFile = open('example.html');
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html-parser')
print(type(exampleSoup))