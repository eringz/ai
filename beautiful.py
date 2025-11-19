import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')

# print(type(elems))
# print(elems[0].attrs)

pElems = exampleSoup.select('p')

# print(pElems)
print(len(pElems))

for i in range(len(pElems)):
    print(pElems[i].getText())
    