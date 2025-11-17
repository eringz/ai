import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

try:
    playFile = open('InventWithPython.txt', 'wb')
    print(res)
    for chunk in res.iter_content(100000):
        playFile.write(chunk)

    print(playFile)
    playFile.close()
except Exception as exc:
    print('There was a proble: %s' % exc)