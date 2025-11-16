import requests

res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
print(type(res))

print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:10])
