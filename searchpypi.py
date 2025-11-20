import requests, sys, webbrowser, bs4

print('Searching...')
# res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))

# res.raise_for_status()

# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# linkElems = soup.select('a')

# print(len(linkElems))

# # for i in range(len(linkElems)):

# numOpen =  min(5, len(linkElems))
# for i in range(numOpen):
#     urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
#     print('Opening', urlToOpen)
#     webbrowser.open(urlToOpen)
#     print(urlToOpen)

