import requests

# res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
# print(type(res))

# print(res.status_code == requests.codes.ok)
# print(len(res.text))
# print(res.text[:10])


# res = requests.get('https://inventwithpython.com/page_that_not_exist');
# print(res.raise_for_status())

res = requests.get('https://inventwithpython.com/page_that_not_exist')

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % exc)